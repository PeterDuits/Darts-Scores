import ipaddress
import re

import src.messages.errors as error_messages
from src.db import database, entities
import src.http.errors as errors


class Validator:
    def __init__(self, session):
        self.session = session

    def validate(self, input_values, rules):
        """Validate input with given rules"""
        self.rules = rules
        self.input = input_values.__dict__
        self.errors = []
        self.stop = False

        # Iterate over fields
        for field in self.rules:
            rules = self.rules.get(field).split('|')
            # Iterate over rules
            for rule in rules:
                # Verify that rule isn't empty
                if rule != '':
                    # Execute correct validation method
                    rule_name, *values = rule.split(':')
                    getattr(self, rule_name + '_rule')(field, values)
                    # Stop validation
                    if self.stop:
                        break

        return self.errors

    def required_rule(self, field, values):
        """Required field"""
        if self.missing(field):
            msg = error_messages.REQUIRED_ERROR.format(field)
            self.errors.append(errors.Error(msg))
            self.stop = True

    def required_without_rule(self, field, values):
        """Required if other field is not present"""
        other_field = values[0]
        if self.missing(field) and self.missing(other_field):
            msg = error_messages.REQUIRED_WITHOUT_ERROR.format(
                field, other_field
            )
            self.errors.append(errors.Error(msg))
            self.stop = True

    def required_with_rule(self, field, values):
        """Required with other field"""
        other_field = values[0]
        if self.missing(field) and self.input.get(other_field):
            msg = error_messages.REQUIRED_WITH_ERROR.format(field, other_field)
            self.errors.append(errors.Error(msg))
            self.stop = True

    def required_if_rule(self, field, values):
        """Required if other field equals certain value"""
        other_field, val = values[0].split(',')
        if self.missing(field) and str(
            self.input.get(other_field)
        ).lower() == str(val).lower():
            msg = error_messages.REQUIRED_IF_ERROR.format(
                field, other_field, val
            )
            self.errors.append(errors.Error(msg))
            self.stop = True

    def not_with_rule(self, field, values):
        """Not with other field"""
        other_field = values[0]
        if self.input.get(field) and self.input.get(other_field):
            msg = error_messages.NOT_WITH_ERROR.format(field, other_field)
            self.errors.append(errors.Error(msg))
            self.stop = True

    def filled_rule(self, field, values):
        """Not empty when present"""
        if self.input.get(field) == '':
            msg = error_messages.FILLED_ERROR.format(field)
            self.errors.append(errors.Error(msg))
            self.stop = True

    def email_rule(self, field, values):
        """Valid email"""
        if self.input.get(field) and not self.valid_email(
            self.input.get(field)
        ):
            msg = error_messages.INVALID_EMAIL_ERROR
            self.errors.append(errors.Error(msg))

    def url_rule(self, field, values):
        """Valid URL"""
        if self.input.get(field) and not self.valid_url(self.input.get(field)):
            msg = error_messages.INVALID_URL_ERROR
            self.errors.append(errors.Error(msg))

    def ip_rule(self, field, values):
        """Valid IP"""
        if self.input.get(field) and not self.valid_ip(self.input.get(field)):
            msg = error_messages.INVALID_IP_ERROR
            self.errors.append(errors.Error(msg))

    def min_rule(self, field, values):
        """Min length"""
        if self.input.get(field):
            length = int(values[0])
            msg = error_messages.MIN_ERROR.format(field, length)
            if len(self.input.get(field)) < length:
                self.errors.append(errors.Error(msg))

    def max_rule(self, field, values):
        """Max length"""
        if self.input.get(field):
            length = int(values[0])
            msg = error_messages.MAX_ERROR.format(field, length)
            if len(self.input.get(field)) > length:
                self.errors.append(errors.Error(msg))

    def in_rule(self, field, values):
        """
            In: The field under validation must be included in the given list
            of values
        """
        if self.input.get(field):
            _values = values[0].split(',')
            msg = error_messages.IN_ERROR.format(field)
            if self.input.get(field) not in _values:
                self.errors.append(errors.Error(msg))

    def alpha_num_space_rule(self, field, values):
        """Only letters, numbers and spaces"""
        if self.input.get(field):
            if not re.match('^[a-zA-Z0-9 ]+$', self.input.get(field)):
                msg = error_messages.ALPHA_NUM_SPACE_ERROR.format(
                    field
                )
                self.errors.append(errors.Error(msg))

    def unique_rule(self, field, values):
        """Unique database record"""
        if self.input.get(field):
            table, col, *extra = values[0].split(',')
            msg = error_messages.UNIQUE_ERROR.format(field)

            ignoreCol = extra[0] if len(extra) > 0 else None
            ignoreVal = extra[1] if len(extra) > 1 else None
            whereCol = extra[2] if len(extra) > 2 else None
            whereVal = extra[3] if len(extra) > 3 else None

            exists = self.unique_check(
                table, col, ignoreCol, ignoreVal, whereCol, whereVal
            )

            if exists:
                self.errors.append(errors.NotUniqueError(msg))

    def exists_rule(self, field, values):
        """Exists in database"""
        if self.input.get(field):
            table, col, *extra = values[0].split(',')
            model = getattr(entities, table.capitalize())

            # Check if extra where is set
            if extra:
                whereCol = extra[0]
                whereVal = extra[1]
                msg = error_messages.EXISTS_WHERE_ERROR.format(
                    field, whereCol
                )
                exists = self.session.query(model).filter(
                    getattr(model, col) == self.input.get(field)
                ).filter(
                    getattr(model, whereCol) == whereVal
                ).first()
            else:
                msg = error_messages.EXISTS_ERROR.format(field)
                exists = self.session.query(model).filter(
                    getattr(model, col) == self.input.get(field)
                ).first()

            if not exists:
                self.errors.append(errors.Error(msg))

    def missing(self, field):
        # Field is missing from input
        if field not in self.input:
            return True

        # Field is present but it's value is None
        if self.input.get(field) is None:
            return True

        # Empty string
        if isinstance(self.input.get(field), str):
            if self.input.get(field).strip() == '':
                return True

        # Empty list
        if isinstance(self.input.get(field), list):
            if len(self.input.get(field)) == 0:
                return True

        return False

    def unique_check(
        self,
        table,
        column,
        ignoreCol=None,
        ignoreVal=None,
        whereCol=None,
        whereVal=None
    ):
        model = getattr(entities, table.capitalize())

        # Create query
        q = self.session.query(model)
        filters = [getattr(model, column) == self.input.get(column)]

        # If ignore values are set
        if (ignoreCol and ignoreVal and ignoreCol != 'null' and
                ignoreVal != 'null'):
            filters.append(getattr(model, ignoreCol) != ignoreVal)

        # If where values are set
        if whereCol and whereVal:
            filters.append(getattr(model, whereCol) == whereVal)
        exists = q.filter(*filters).first()

        return exists

    def camel_to_snake(self, s):
        return re.compile(r'(?!^)(?<!_)([A-Z])').sub(r'_\1', s).lower()

    def valid_email(self, email):
        return re.match(
            "^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]" +
            "+(?:\.[a-zA-Z0-9-]+)*$",
            email
        )

    def valid_url(self, url):
        return not url.startswith('http://') and not url.startswith('https://')

    def valid_ip(self, ip):
        try:
            ipaddress.ip_address(ip)
            return True
        except:
            return False
