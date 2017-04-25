FROM python:2.7-alpine

RUN \
  apk add --update --no-cache bash ffmpeg git python python-dev py-pip && \
  pip install -U Flask youtube-dl bs4 awscli && \
  apk del git python-dev

EXPOSE 5010

RUN mkdir -p /src/tmp

COPY . /src

WORKDIR /src

CMD ["python", "/src/app.py"]
