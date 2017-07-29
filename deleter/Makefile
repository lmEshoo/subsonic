.PHONY: helping hand

IMAGE=lmestar/sub-deleter
CONTAINER_NAME=sub-deleter
PORT=5050
all: build run

build:
	 docker build -t $(IMAGE) .

run: build
	 docker run \
		--name=$(CONTAINER_NAME) --rm \
		-v /var/music:/var/music -v /var/s3:/var/s3 -v ${PWD}:/src \
		-e AWS_ACCESS_KEY_ID=${AWS_SUB_ACCESS_KEY_ID} \
 		-e AWS_SECRET_ACCESS_KEY=${AWS_SUB_SECRET_ACCESS_KEY} \
		-e INSTANCE_IP=${INSTANCE_IP} \
		-e SUB_USER=${SUB_USER} \
 		-e SUB_PASS=${SUB_PASS} \
		-d $(IMAGE)

clean:
	 docker stop $(CONTAINER_NAME)
	 docker rm $(CONTAINER_NAME)

restart: clean run
	docker logs -f sub-recommendr

go: build
	docker run \
		--name=$(CONTAINER_NAME) --rm -v ${PWD}:/src \
		-v /var/music:/var/music -v /var/s3:/var/s3 \
		-e AWS_ACCESS_KEY_ID=${AWS_SUB_ACCESS_KEY_ID} \
 		-e AWS_SECRET_ACCESS_KEY=${AWS_SUB_SECRET_ACCESS_KEY} \
		-e INSTANCE_IP=${INSTANCE_IP} \
		-e SUB_USER=${SUB_USER} \
 		-e SUB_PASS=${SUB_PASS} \
		-it --entrypoint=bash $(IMAGE)

exec:
	docker exec -it $(CONTAINER_NAME) bash
