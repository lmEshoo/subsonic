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
    spotipy \
    boto3 && \
  apk del git python-dev

EXPOSE 5050

RUN mkdir -p /src/tmp

COPY . /src

WORKDIR /src

CMD ["python", "/src/run.py"]
