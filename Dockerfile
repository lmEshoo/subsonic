FROM hypriot/rpi-java:jre-1.8.111

MAINTAINER liniMestar@gmail.com

USER root

RUN \
  apt-get -y update && \
  apt-get install -y python-pip wget && \
  pip install awscli && \
  rm -rf /var/lib/apt/lists/* && \
  echo "exit 0">/usr/sbin/policy-rc.d && \
  mkdir -p /app

EXPOSE 4040

WORKDIR /app

RUN \
  chown -R root:users /app && \
  wget \
  https://downloads.sourceforge.net/project/subsonic/subsonic/6.0/subsonic-6.0.deb && \
  dpkg -i /app/subsonic-6.0.deb

ADD . /app

CMD sh getMusic.sh && \
  dpkg -i /app/subsonic-6.0.deb && \
  sleep 1 && tail -f /var/subsonic/subsonic_sh.log
