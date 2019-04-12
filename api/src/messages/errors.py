UNAUTHORIZED = "This action requires authorization."
PERMISSION_DENIED = "Permission denied."

CUSTOMER_NOT_FOUND = "Customer doesn’t exist."
ADDRESS_NOT_FOUND = "Address not found."

INVALID_TOKEN_FORMAT = "Invalid token format."

AUTH_ERROR = "Invalid credentials."

REQUIRED_ERROR = "The '{}' field is required."
REQUIRED_WITHOUT_ERROR = "The '{}' field or the '{}' field is required."
REQUIRED_WITH_ERROR = "The '{}' field is required if the '{}' field is " \
                      "present."
REQUIRED_IF_ERROR = "The '{}' field is required if the '{}' field equals '{}'."
FILLED_ERROR = "The '{}' field must not be empty when it is present."
INVALID_EMAIL_ERROR = "Invalid email address."
INVALID_URL_ERROR = "Invalid url. A url must start with http:// or https://."
INVALID_IP_ERROR = "Invalid ip address."
MIN_ERROR = "The '{}' field has to be at least '{}' characters."
MAX_ERROR = "The '{}' field cannot be longer than '{}' characters."
IN_ERROR = "The '{}' field has an invalid value."
ALPHA_NUM_SPACE_ERROR = "The '{}' field can only contain letters, numbers " \
                        "and spaces."
UNIQUE_ERROR = "A record with this '{}' aleady exists."
EXISTS_ERROR = "A record with this '{}' does not exists."
EXISTS_WHERE_ERROR = "A record with this '{}' does not exists for the given " \
                     "'{}'."
NOT_WITH_ERROR = "The '{}' field can’t be present when the '{}' field is " \
                 "present."


PAYMENT_GATEWAY_ERROR = "[{}] Payment Gateway Error: ({}) {}"
PAYMENT_GATEWAY_TIMEOUT = "The payment service is temporarily unavailable, " \
                          "please try again later."
TRANSACTION_NOT_FOUND = "Transaction not found."
TRANSACTION_NOT_INITIATED = "A transaction has not been initiated for this " \
                            "checkout yet. The pay checkout mutation has to " \
                            "be called first."
TRANSACTION_ALREADY_COMPLETED = "A transaction for this checkout has already" \
                                " been completed."
TRANSACTION_NOT_YET_COMPLETED = "This transaction has not been completed yet."
TRANSACTION_REFUND_EXISTS = "This transaction has already been refunded or " \
                            "is in the process of being refunded."
TRANSACTION_NON_REFUNDABLE = "The payment product ({}) used for this " \
                             "transaction is non refundable."
CHECKOUT_NOT_COMPLETE_ERROR = "This checkout still has errors or is missing " \
                              "certain fields. Please use the update " \
                              "checkout mutation to update the checkout " \
                              "accordingly."
CHECKOUT_TRANSACTION_NOT_YET_COMPLETED = "A transaction for this checkout " \
                                         "has not yet been completed"
SHIPPING_GATEWAY_TIMEOUT = "The shipping service is temporarily unavailable" \
                           ", please try again later."
SHIPPING_NOT_REQUIRED = "The line items in this checkout don’t require " \
                        "shipping."
SHIPMENT_ALREADY_CREATED = "A shipment has already been created for this " \
                           "checkout."
SHIPMENT_NOT_FOUND = "The specified shipment could not be found."
IDEAL_UNSUPPORTED_CURRENCY = "To accept iDEAL as a payment product the " \
                             "store’s currency needs to be EUR."
INVALID_IDEAL_ISSUER = "Invalid iDEAL issuer specified."
UNSUPPORTED_PAYMENT_PRODUCT = "The selected payment product ({}) is not " \
                              "supported by this store."
EMAIL_SERVICE_ERROR = "The email service is temporarily unavailable, " \
                      "please try again later."
PASSWORD_RESET_NOT_FOUND = "The provided details do not match a password " \
                           "reset record in our database."
