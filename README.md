# Cloud Project
## Project for Cloud Computing exam

##  Tasks
Identifying, deploying and implementing a cloud-based file storage system. The system should allow users to upload, download and delete files. Each user should have a private storage space. The system should be scalable, secure, and cost-efficient.

## Documentation, Code and Presentation

In this repository, will be available: 

- Report where is explained and described the project architecture;
- Docker files and any code developed/modified for the cloud-based file storage system;
- A short presentation summarizing the design and implementation (w.i.p.).

## How to deploy and use the system

The system is deployed using Docker and Docker Compose. To deploy the system, is needed to have Docker and Docker Compose installed on your machine. It is possible to check if you have Docker and Docker Compose installed by running the following commands:

```bash
docker --version
docker-compose --version
```

Then, you can clone this repository and run the following command to deploy the system (make sure you are in the root directory of the repository):

```bash
docker-compose up -d
```

The system will be deployed and you can access it by going to `http://localhost:8080` in your browser.

## Inside the Docker Compose configuration

The file `docker-compose.yml` contains the configuration for the system, specifying how Docker containers should be run for a multi-service setup. The services defined include:

- `nextcloud` - This is a container for the Nextcloud application, an open-source file sync and share solution. It uses  `nextcloud` image, maps port 8080 on the host to port 80 on the container, uses a volume for persistent storage and it depends on the `db` service;
- `db` - This container runs a MariaDB database, an open-source relational database management system. It uses the mariadb image, sets various environment variables for MySQL configuration, and uses a volume for data persistence;
- `prometheus` - This container runs Prometheus, an open-source monitoring system with a time series database. It uses the prom/prometheus image, mounts a configuration file from the host, and exposes port 9090;
- `grafana` - : This service uses the grafana/grafana image for running Grafana, an open-source platform for monitoring and observability. It mounts a volume for data, sets an admin password through an environment variable, and maps port 3000;
- `node exporter` - This service uses the prom/node-exporter image to run Node Exporter, which exports hardware and OS metrics. It exposes port 9100.

The file also defines volumes for nextcloud, db, and grafana_data for data persistence. There are commented placeholders for additional services like Redis (a caching service), and a load balancer (like Nginx or HAProxy), as well as for network configurations.

## Locust for testing

Locust is an open-source load testing tool used to test the performance of web applications. It's designed to help developers simulate loads of various types on a system or a server, primarily to check how much traffic the system can handle before it becomes unresponsive or slows down significantly.

Locust is a Python-based tool, so it is needed to have Python installed on machine. To install Locust, run the following command:

```bash
pip install locust
```

or

```bash
brew install locust
```
From the root directory of the repository, run the following command to start the Locust web interface:

```bash
./locust_load.sh
```
Where it was already defined the testing scenario inside the Python script `test_incr.py` and `test_two.py`. 

## Ports

|    |   Port |
| -------- | ------|
| Nextcloud | [8080](http://localhost:8080) |
| Grafana | [3000](http://localhost:3000) |
| Prometheus | [9090](http://localhost:9090) |
| Locust | [8089](http://localhost:8089) |



More details on how to use the system will be available in the README file in the root directory of the repository. The README file will contain instructions on how to upload, download and delete files, as well as how to create new users and manage the system and the tests performed. 

## Author

- [@abandrea](https://github.com/abandrea) - **Andrea Buscema**, MSc student in Data Science and Artificial Intelligence, University of Trieste


## License

[MIT](https://choosealicense.com/licenses/mit/)
