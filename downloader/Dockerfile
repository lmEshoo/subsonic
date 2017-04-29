FROM python:2.7-slim

MAINTAINER liniMestar@gmail.com

RUN \
  apt-get update -qq && \
  apt-get install -y --no-install-recommends \
    bash \
    libav-tools \
    git \
    python \
    python-dev \
    python-pip && \
  pip install -U \
    Flask \
    youtube-dl \
    bs4 \
    awscli \
    instantmusic \
    fixalbumart \
    eyed3 \
    requests && \
  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 5010

RUN mkdir -p /src/tmp

COPY . /src

WORKDIR /src

CMD ["python", "/src/app.py"]
