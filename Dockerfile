FROM hypriot/rpi-java:jre-1.8.111

MAINTAINER liniMestar@gmail.com

USER root

RUN \
  apt-get -y update && \
  apt-get install -y \
    python-pip \
    curl \
    wget && \
  pip install -U \
    awscli \
    eyed3 \
    requests && \
  rm -rf /var/lib/apt/lists/* && \
  echo "exit 0">/usr/sbin/policy-rc.d && \
  mkdir -p /app && \
  mkdir -p /var/s3 && \
  easy_install pathlib

EXPOSE 4040

WORKDIR /app

ARG SUB_VERSION

RUN \
  chown -R root:users /app && \
  wget \
  https://s3-eu-west-1.amazonaws.com/subsonic-public/download/subsonic-${SUB_VERSION}.deb \
  -O /app/subsonic.deb && \
  dpkg -i /app/subsonic.deb

ADD . /app

CMD \
  bash /app/tools/getMusic.sh && \
  dpkg -i /app/subsonic.deb && \
  bash /app/tools/sub-dl.sh post && \
  sleep 1 && tail -f /var/subsonic/subsonic_sh.log
