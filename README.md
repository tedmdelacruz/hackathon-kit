# Prototype Kit

This is a starter kit for prototyping web applications, APIs, and mobile app ideas.

**Powered by:** 
* Django
* Django REST Framework
* MySQL
* React Native
* MobX
* VueJS
* Redis

**TODO:**
- [x] Setup Django REST Framework Docker image as server
- [x] Create GET /users endpoint
- [x] Use built-in authentication of Django
- [x] Add simple registration and login page
- [x] Replace SQLite3 with MySQL
- [ ] Setup localtest
- [ ] Setup Redis
- [ ] Setup React Native and MobX with server
- [x] Setup VueJS SPA interacting with server
- [ ] Setup Django Admin
- [ ] Setup Facebook login
- [ ] Setup unit tests
- [ ] Setup Circle CI
- [ ] Setup codecov
- [ ] Setup automated deployment
- [ ] Deploy on AWS

## API
**URL** http://api.localtest.me:8000

### Setup

```
cd api
mv .env.example .env
vim .env # Update this
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
