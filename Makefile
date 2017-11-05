SHELL := /bin/sh

PROJECT_NAME := proto
DB_CONTAINER := proto_db
SERVER_CONTAINER := proto_server
DOCKER_COMPOSE_FILE := server/docker-compose.yml

init:
	docker-compose -f $(DOCKER_COMPOSE_FILE) --project-name $(PROJECT_NAME) build

up:
	docker-compose -f $(DOCKER_COMPOSE_FILE) --project-name $(PROJECT_NAME) up -d

down:
	docker-compose -f $(DOCKER_COMPOSE_FILE) --project-name $(PROJECT_NAME) down

logs:
	docker logs -f $(SERVER_CONTAINER)

migrate:
	docker exec $(SERVER_CONTAINER) ./manage.py migrate

superuser:
	docker exec -it $(SERVER_CONTAINER) ./manage.py createsuperuser

test:
	docker exec $(SERVER_CONTAINER) ./manage.py test
