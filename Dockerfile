FROM hypriot/rpi-java:jre-1.8.111

MAINTAINER liniMestar@gmail.com

USER root

RUN \
  apt-get -y update && \
  apt-get install -y python-pip curl wget && \
  pip install awscli && \
  rm -rf /var/lib/apt/lists/* && \
  echo "exit 0">/usr/sbin/policy-rc.d && \
  mkdir -p /app

EXPOSE 4040

WORKDIR /app

RUN \
  chown -R root:users /app && \
  wget \
  https://s3-eu-west-1.amazonaws.com/subsonic-public/download/subsonic-6.1.beta2.deb && \
  dpkg -i /app/subsonic-6.1.beta2.deb

ADD . /app

ADD setSubCoverArt.py /var/music/

CMD \
  bash getMusic.sh && \
  dpkg -i /app/subsonic-6.1.beta2.deb && \
  bash sub-dl.sh post && \
  sleep 1 && tail -f /var/subsonic/subsonic_sh.log
