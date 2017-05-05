.PHONY: helping hand

IMAGE=lmestar/sub-recommendr
CONTAINER_NAME=sub-recommendr
PORT=5050
all: build run

build:
	 docker build -t $(IMAGE) .

run: build
	 docker run \
		--name=$(CONTAINER_NAME) \
		-e AWS_ACCESS_KEY_ID=${AWS_SUB_ACCESS_KEY_ID} \
 		-e AWS_SECRET_ACCESS_KEY=${AWS_SUB_SECRET_ACCESS_KEY} \
		-e SPOTIPY_CLIENT_ID=${SPOTIPY_CLIENT_ID} \
 		-e SPOTIPY_CLIENT_SECRET=${SPOTIPY_CLIENT_SECRET} \
		-e SPOTIPY_REDIRECT_URI=${SPOTIPY_REDIRECT_URI} \
		-e INSTANCE_IP=${INSTANCE_IP} \
		-d -p $(PORT):$(PORT) $(IMAGE)

clean:
	 docker stop $(CONTAINER_NAME)
	 docker rm $(CONTAINER_NAME)

restart: clean run

go: build
	docker run \
		--name=$(CONTAINER_NAME) \
		-e AWS_ACCESS_KEY_ID=${AWS_SUB_ACCESS_KEY_ID} \
 		-e AWS_SECRET_ACCESS_KEY=${AWS_SUB_SECRET_ACCESS_KEY} \
		-e SPOTIPY_CLIENT_ID=${SPOTIPY_CLIENT_ID} \
 		-e SPOTIPY_CLIENT_SECRET=${SPOTIPY_CLIENT_SECRET} \
		-e SPOTIPY_REDIRECT_URI=${SPOTIPY_REDIRECT_URI} \
		-e INSTANCE_IP=${INSTANCE_IP} \
		-it --entrypoint=bash \
		-p $(PORT):$(PORT) $(IMAGE)

exec:
	docker exec -it $(CONTAINER_NAME) bash
