FROM python:3.7.2

RUN apt-get update && apt-get -y install libxml2-dev libxmlsec1-dev libxmlsec1-openssl

WORKDIR /usr/src/app

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pip install pip --upgrade
RUN pip install pipenv --upgrade \
    && pipenv install --deploy --system --dev