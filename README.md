# Django Kit

This is my personal starter kit for prototyping Django Progressive Web Apps

**Powered by:** 
* Django 2
* PostgreSQL
* Redis
* VueJS

**TODO:**
- [ ] Improve Docker server start procedure
- [ ] Setup multi-level authorization
- [ ] Setup localtest
- [ ] Setup Celery
- [ ] Setup Django Admin
- [ ] Setup Facebook login
- [ ] Setup unit tests
- [ ] Setup Travis CI
- [ ] Setup codecov
- [ ] Setup automated deployment
- [ ] Deploy on AWS
- [ ] Setup payment system

### Setup

```
cd src
mv .env.example .env
vim .env # Update this
docker-compose build
docker-compose up -d 
```

## Web
**URL** http://web.localtest.me:8080

### Setup

```
yarn
npm run start
npm run server
```
