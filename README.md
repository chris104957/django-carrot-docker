# django-carrot-docker
A docker example for django-carrot, using:
- Django
- Postgres
- RabbitMQ
- django-carrot

## Prerequisites
- docker
- docker-compose

## Installation
1. Clone repo
```
git clone https://github.com/chris104957/django-carrot-docker.git
```

2. Build it
```
cd django-carrot-docker
docker-compose build
```

3. Run it
```
docker-compose run
```

4. Test it
- Go to http://localhost/carrot > Scheduled> Create New
    - task: app.tasks.hello_world
    - queue: default
    - interval: every 5 seconds
    - active: true
- Save
