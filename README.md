# docker playground
Dockerizing 2 services:
- ssh: create SSH server with sshd
- http: create webserver with flask that is behind nginx

# Prerequisites
Docker and docker-compose are required, see:
[docker docs](https://docs.docker.com/engine/installation/).
[docker-compose docs]( https://docs.docker.com/compose/)

## Execution
To start the project build the containers:
```bash

docker-compose build

```
Then run them:
```bash
docker-compose up
```

## Tests
Tests are found: sshd/modules/tests.py
In order to execute all:
```bash
sudo py.test tests.py
```
or specific test case:
```bash
sudo py.test tests.py -k <tc_name>
```

## Possible improvements for the future
* set database instead of using excel database
* increase the api test scope of post, put, delete methods
* set LDAP (initd and systemd inside container) on ssh container to verify users
* develop the html/css on the website
* create better test case description and exception handling

## Built With
* [Docker](https://docs.docker.com) - Standardizing environment.
* [Flask](http://flask.pocoo.org/docs/1.0/) - The web framework used.
* [nginx](https://nginx.org/en/docs/) - Proxy.
