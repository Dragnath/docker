# docker
Dockerizing ssh and http services.

# Prerequisites
Docker installation is required, see the [official installation docs](https://docs.docker.com/engine/installation/).

## Execution
To start the project build the containers:
```bash
docker-compose build
```
Then run them:
```bash
docker-compose up
```

## Built With

* [Docker](https://docs.docker.com) - Standardizing environment.
* [Flask](http://flask.pocoo.org/docs/1.0/) - The web framework used.
* [nginx](https://nginx.org/en/docs/) - HTTP server.
