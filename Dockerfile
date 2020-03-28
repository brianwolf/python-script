FROM python:3.8-alpine

WORKDIR /usr/src/

ARG TAG=1.0.0


# DEPENDENCIAS
COPY ./src/requirements.txt .
RUN pip install -r requirements.txt --upgrade pip


# VARIABLES PREDEFINIDAS
ENV VERSION=${TAG}


# CODIGO FUENTE
COPY ./scripts .
COPY ./src/ .


# COMPILACION
RUN ./scripts/build.sh