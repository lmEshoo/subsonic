.PHONY: helping hand

IMAGE=lmestar/sub-dl
CONTAINER_NAME=sub-dl

all: build run

build:
	docker build -t $(IMAGE) .

run: build
	docker run \
		--name=$(CONTAINER_NAME) \
		-e AWS_ACCESS_KEY_ID=${AWS_SUB_ACCESS_KEY_ID} \
 		-e AWS_SECRET_ACCESS_KEY=${AWS_SUB_SECRET_ACCESS_KEY} \
		-d -p 5010:5010 $(IMAGE)

clean:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)

go: build
	docker run \
		--name=$(CONTAINER_NAME) \
		-e AWS_ACCESS_KEY_ID=${AWS_SUB_ACCESS_KEY_ID} \
 		-e AWS_SECRET_ACCESS_KEY=${AWS_SUB_SECRET_ACCESS_KEY} \
		-it --entrypoint=sh \
		-p 5010:5010 $(IMAGE)

exec:
	docker exec -it $(CONTAINER_NAME) sh
