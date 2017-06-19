.PHONY: helping hand

IMAGE=lmestar/subsonic

CONTAINER_NAME=subsonic

VERSION=6.1

all: down up

build:
	 docker build --build-arg SUB_VERSION=$(VERSION) -t $(IMAGE) .

run: build
	 sudo docker run \
		--name=$(CONTAINER_NAME) -v /var/music:/var/music \
		-e AWS_ACCESS_KEY_ID=${AWS_SUB_ACCESS_KEY_ID} \
 		-e AWS_SECRET_ACCESS_KEY=${AWS_SUB_SECRET_ACCESS_KEY} \
		-e INSTANCE_IP=${INSTANCE_IP} \
		-e SUB_USER=${SUB_USER} \
 		-e SUB_PASS=${SUB_PASS} \
		-d -p 4040:4040 $(IMAGE)

go: build
	sudo docker run \
		--name=$(CONTAINER_NAME) -v /var/music:/var/music \
		-e AWS_ACCESS_KEY_ID=${AWS_SUB_ACCESS_KEY_ID} \
		-e AWS_SECRET_ACCESS_KEY=${AWS_SUB_SECRET_ACCESS_KEY} \
		-e INSTANCE_IP=${INSTANCE_IP} \
		-e SUB_USER=${SUB_USER} \
		-e SUB_PASS=${SUB_PASS} \
		-it --entrypoint=bash \
		-p 4040:4040 $(IMAGE)

up: run

down:
	 docker stop $(CONTAINER_NAME)
	 docker rm $(CONTAINER_NAME)

start: flask_up

flask_up: up dl_up rec_up
	 cd Flask && nohup python app.py & #>/dev/null 2>&1

dl_up:
	sh sub-dl.sh up

rec_up:
	sh sub-dl.sh rec

clean: down
	sh sub-dl.sh down
