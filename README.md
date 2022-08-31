# Online Shop website
This is an Online Shop website created with Django


## Use RabbitMQ and Celery

run rabbitmq

```docker
docker run -d --hostname my-rabbit --name some-rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9.22-management-alpine
```

### run celery

```sh
celery -A config worker -l info
```

### run flower for monitoring celery

```sh
celery -A config flower
```

### create a network for redis

```sh
docker network create -d bridge redisnet
```

### run the redis container

```sh
docker run -d -p 6379:6379  --name bookmark-redis --network redisnet redis:alpine
```