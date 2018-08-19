# Django Kit

This is my personal starter kit for prototyping Django Progressive Web Apps

**_Discontinued_** I decided to just use [https://cookiecutter-django.readthedocs.io/en/latest/](cookie-cutter-django) which is much better

**Powered by:** 
* Django 2
* MySQL
* Redis
* Vue

### Setup

```
cd src
mv .env.example .env
vim .env # Update this
docker-compose build
docker-compose up -d 

yarn
npm run start/build
```

### Debugging with ipdb

Stop `web` container then run

```sh
docker-compose run --service-ports web
```
