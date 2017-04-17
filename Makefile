.PHONY: helping hand

IMAGE=lmestar/subsonic

CONTAINER_NAME=subsonic

all: build aws

build:
	docker build -t $(IMAGE) .

aws:
	docker run --rm \
		--name=$(CONTAINER_NAME) \
		-e AWS_ACCESS_KEY_ID=${AWS_SUB_ACCESS_KEY_ID} \
		-e AWS_SECRET_ACCESS_KEY=${AWS_SUB_SECRET_ACCESS_KEY} \
		-p 4040:4040 $(IMAGE)

stop:
	docker stop $(CONTAINER_NAME)
