.PHONY: helping hand

IMAGE=lmestar/subsonic

CONTAINER_NAME=subsonic

all: down up

up:
	docker-compose up -d $(CONTAINER_NAME)

down:
	docker-compose kill $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)

build:
	docker build -t $(IMAGE) .

start: flask_up

flask_up: up dl_up
	 cd Flask && nohup python app.py &
	 #cd Flask && python app.py

dl_up:
	sh sub-dl.sh up

clean: down
	sh sub-dl.sh down
	kill -9 `ps -aux | grep python | grep -v grep | awk '{ print $2 }'`
