# Project of Cloud Basic

## Deployment Plan using Docker and Docker-Compose

After choosing between Nextcloud and MinIO, it was planned the deployment on laptop in a containerized environment using Docker and Docker-Compose.

### Install Docker and Docker-Compose

First, it is necessary to install Docker and Docker-Compose. On MacOS, it is possible to install Docker Desktop, which includes Docker-Compose. (On Linux, it is possible to install Docker and Docker-Compose separately.)

To install Docker Desktop, it is necessary to download the installer from the official website: https://www.docker.com/products/docker-desktop

After downloading the installer, it is necessary to run it and follow the instructions. After the installation, it is possible to check if Docker and Docker-Compose are installed using the following commands:

```bash
docker --version
docker-compose --version
```

If Docker and Docker-Compose are installed, the commands will return the version of the installed software.

Otherwise, it is possible to install Docker and Docker-Compose using Homebrew:

```bash
brew install docker docker-compose
```

### Create Docker-Compose File

After installing Docker and Docker-Compose, it is necessary to create a Docker-Compose file to define the services that will be used in the deployment. The Docker-Compose file is a YAML file that defines the services, networks, and volumes that will be used in the deployment.

The Docker-Compose file for the deployment of Nextcloud is as follows:

```yaml
version: '3'

services:
  db:
    image: mariadb
    command: --transaction-isolation=READ-COMMITTED --binlog-format=ROW
    restart: always
    volumes:
      - db:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: example
      MYSQL_PASSWORD: example
      MYSQL_DATABASE: example
      MYSQL_USER: example

  app:
    image: nextcloud
    ports:
      - 8080:80
    links:
      - db
    volumes:
      - nextcloud:/var/www/html
    restart: always
    environment:
      MYSQL_HOST: db
      MYSQL_DATABASE: example
      MYSQL_USER: example
      MYSQL_PASSWORD: example

```
Here is where it's possible to include choosen file storage system, database service (if required), and any other necessary service.

For what concerns database, it was used MariaDB, which is a community-developed fork of MySQL, and it is one of the most popular database servers in the world. It is included in the Docker-Compose file as a service, and it is linked to the Nextcloud service. The MariaDB service is defined with the image mariadb, and it is configured with the environment variables MYSQL_ROOT_PASSWORD, MYSQL_PASSWORD, MYSQL_DATABASE, and MYSQL_USER. The volumes section is used to define the volume that will be used to store the database data. The restart section is used to define the restart policy for the service. The command section is used to define the command that will be used to start the service. The links section is used to define the link between the MariaDB service and the Nextcloud service. 

For what concerns Nextcloud, it is included in the Docker-Compose file as a service, and it is linked to the MariaDB service. The Nextcloud service is defined with the image nextcloud, and it is configured with the environment variables MYSQL_HOST, MYSQL_DATABASE, MYSQL_USER, and MYSQL_PASSWORD. The volumes section is used to define the volume that will be used to store the Nextcloud data. The restart section is used to define the restart policy for the service. The ports section is used to define the port that will be used to access the Nextcloud service. The links section is used to define the link between the Nextcloud service and the MariaDB service.

### Deploy Services using Docker-Compose

After creating the Docker-Compose file, it is possible to deploy the services using Docker-Compose. To deploy the services, it is necessary to run the following command in the directory where the Docker-Compose file is located:

```bash
docker-compose up -d
```

The command will start the services in the background, and it will create the necessary networks and volumes. After the services are started, it is possible to check the status of the services using the following command:

```bash
docker logs
```

The command will return the status of the services, and it will show if the services are running or not. If the services are running, it is possible to access the Nextcloud service using a web browser. The Nextcloud service can be accessed at the following URL:

```bash
http://localhost:8080
```

After accessing the Nextcloud service, it is possible to create an account and start using the service. The Nextcloud service can be used to store files, share files, and collaborate with others. It is also possible to install apps and plugins to extend the functionality of the service.

What I used is Docker Desktop for MacOS. It's user friendly and easy to use. It's possible to manage containers, images, networks, and volumes using the Docker Desktop interface. It's also possible to view the logs of the services, and to stop and remove the services using the Docker Desktop interface.

## Explanation of the Deployment Plan with Docker and Docker-Compose

Deploying Nextcloud with Docke Compose involves several steps, each focusing on creating an isolated yet interconnected environment where NExtcloud can operate with its required services.

### Structure of Docker Compose File

The file is structured in a specific format that docker Compose understands. It begins with a version declaration (version: '3') that specifies the version of the Compose file format. It then contains definitions for different sections, such as services, networks, and volumes. 

### Defining Services

- **Database Service**: A database is essential for Nextcloud to store data. It is possible to define a service (often named `db` for simplicity) using a database image MySQL or MariaDB. It is possible also to set environment variables (like root password, database name, and user credentials) required for the database configuration.

- **Nextcloud Service**: This is the main application service that runs the Nextcloud image. The `image` tag is used to specify the Nextcloud image. The `ports` section maps the ports of the container to your host machine, allowing to access Nextcloud via a web browser. The `links` tag is used to link this service to the database service, allowing Nextcloud to access the database. Environment variables can be set to configure the connection to the database (like database name, user, and password). The `volumes` tag is used for data persistance. Without this, all data stored in Nextcloud would be lost when the container is stopped. 


## Accessing Nextcloud

After running the `docker-compose up -d` command, Nextcloud can be accessed at `http://localhost:8080` in a web browser. The initial setup involves creating an admin account and configuring the database settings. Once the setup is complete, Nextcloud is ready to use.

In Docker Desktop, just easily click on the container and click on play button to start the container. It's also possible to view the logs of the services, and to stop and remove the services using the Docker Desktop interface.

To stop the services, it is possible to click on the stop button in the Docker Desktop interface, or to run the following command in the directory where the Docker-Compose file is located:

```bash
docker-compose down
```

The command will stop the services and remove the networks and volumes that were created. After the services are stopped, it is possible to remove the containers and images using the Docker Desktop interface. It's also possible to remove the containers and images using the following commands:

```bash
docker container rm <container_id>
docker image rm <image_id>
```

The commands will remove the containers and images that were created. After the containers and images are removed, it is possible to remove the networks and volumes using the Docker Desktop interface. It's also possible to remove the networks and volumes using the following commands:

```bash
docker network rm <network_id>
docker volume rm <volume_id>
```

The commands will remove the networks and volumes that were created. 


## Initial Setup of Nextcloud

Once the containers are up and running, it is possible to access Nextcloud at `http://localhost:8080` in a web browser. The initial setup involves creating an admin account, choosing an username and  a strong password. 

### Tests and Checks

After the initial setup, it is possible to test the functionality of Nextcloud by uploading files, creating folders, and sharing files with others. It is also possible to install apps and plugins to extend the functionality of the service. Doing this can help to ensure that Nextcloud is working as expected and that it is ready to use. It also needed to check and make sure that Nextcloud is correclty connected to the database and that the data is being stored correctly.

## Management and Maintenance 

This part is crucial for ensuring the long-term stability and security of the setup. 

General management tasks include:
- Regularly updating for both Nextcloud and the database;
- Backup strategy, which includes regular backups of the database and Nextcloud data;
- Regularly review user accounts and permissions to ensure that access levels are appropriate;
- Monitoring disk usage and performance to ensure that the system is running smoothly.

General Maintenance tasks include:
- Perform regular health checks, it can be easily done using built in tools under the admin settings to check the health and performance of the system;
- Regularly check logs for any errors or warnings;
- Security Checks, it is important to regularly review and update security settings to ensure that the system is secure. If the system is exposed to the internet, it is important to consider additional security measures such implementing SSL/TLS certificates and using a firewall.
- Regularly update passwords and employ strong authentication methods. 
- Performance tuning, such as adjusting php settings, fine-tuning database parameters, or scaling your Docker resources.

## Scalability Aspects

### Horizontal vs. Vertical Scaling

- **Vertical Scaling**: This involves increasing the capacity and the power of the server by adding more resources (CPU, RAM, etc.) to the existing server. This is often done by upgrading the hardware of the server. This approach has its limitations, like physical and cost limits.

- **Horizontal Scaling**: This involves adding more servers to the existing infrastructure. This approach is more flexible and scalable, as it allows to distribute the load across multiple servers. This approach is often used in cloud environments, where it is possible to add or remove servers as needed.


