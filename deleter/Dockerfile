FROM rcarmo/alpine-python:2.7.12-armhf

MAINTAINER liniMestar@gmail.com

RUN \
  apk add --update --no-cache \
    bash \
    curl \
    python \
    python-dev \
    py-pip && \
  pip install -U \
    Flask \
    bs4 \
    requests \
    boto3 && \
  apk del git python-dev

ADD . /src

WORKDIR /src

ENTRYPOINT ["python","app.py"]
