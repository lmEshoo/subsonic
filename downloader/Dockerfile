FROM python:2.7-slim

RUN \
  apt-get update && \
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
    requests \
  && rm -rf /var/lib/apt/lists/*

EXPOSE 5010

RUN mkdir -p /src/tmp

COPY . /src

WORKDIR /src

CMD ["python", "/src/app.py"]
