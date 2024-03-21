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

## Inside the docker

Inside the docker, there are 5 containers:

- `nextcloud` - the main container, where the Nextcloud instance is running: 
- `db` - the database container, where the MariaDB instance is running;
- `prometheus` - the Prometheus container, which is used to monitor the system;
- `grafana` - the Grafana container, which is used to visualize the data collected by Prometheus;
- `node exporter` - the Node Exporter container, which is used to collect data from the system and send it to Prometheus.



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
