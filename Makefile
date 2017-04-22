.PHONY: helping hand

IMAGE=lmestar/subsonic

CONTAINER_NAME=subsonic

all: down up

up:
	docker-compose up -d

down:
	docker-compose kill
	docker-compose down

build:
	docker build -t $(IMAGE) .

start:
	cd Flask && nohup python app.py &
