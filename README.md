# Cloud_project
## Project for cloud exam

##  Taks
Identifying, deploying and implementing a cloud-based file storage system. The system should allow users to upload, download and delete files. Each user should have a private storage space. The system should be scalable, secure, and cost-efficient.

It was suggested solutions to use for exam between Nextcloud (https://nextcloud.com/) and MinIO (https://min.io/).

First of all, it's necessary to explain what are Nextcloud and MinIO: 

Nextcloud and MinIO are both cloud storage solutions, but they serve in different ways and have different features, which could influence the decision of choosing one versus the other. 

### Nextcloud

Nextcloud was primarily designed for file sharing and collaboration platform, if offers features like file synchronization, calendar, contacts, mail, and task management toold. It's often (and easily) seen as an alternative to services like Google Drive (https://www.google.com/drive/) or Dropbox (https://www.dropbox.com/), with a strong emphasis on **privacy and self-hosting**. It offers a wide range of features including end-to-end encryption, two-factor authentication, collaboration tools and integration with third-party applications. It's more user-friendly for non-technical users, for example it provides a web interface, desktop clients and mobile apps, making it accessible for a wide range of users. It's also easy to deploy for smaller to medium-sized installations (it can be scaled, but may require additional configuration and hardware for very large deployments). Lastly, has a large community and offers professional support services.

### MinIO

MinIO it's an high-performance, distributed object storage system desiged for large-scale private cloud infrastructures. It is API-compatible with Amazon S3, making it suitable for enterprises looking for a private or hybrid cloud storage solution. MinIO focuses ore on the storage aspect rather than collaboration tools. It's specialized and optimized for machine learning, analytics and application data, and offers features like erasure coding and bitrot protection for data integrity. Instead of Nextcloud, MinIO focuses more on API access and is typically managed via command line, though it does have a basic web interface for management tasks (that, from my personal opinion, it can be always appreciate). MinIO was deisgned for large-scale deployment from the start, easily scalable and can handle petabytes of data and high levels of throughput. Also, has a strong community support, with enterprise support available. It's often favored in enterprise environments with large-scale storage needs.

### Choice and reason 

Regarding project tasks, the first choice fell on Nextcloud. The reasons are:

- file sharing and collaboration with user-friendly interface, including non-technical users;
- strong privacy controls and open-source software;
- small to medium-sized stogare needs and an easy-to-deploy solution.

In contrast, in real world use with big data projects, where primary requirements is high-performance, scalable object storage, MinIO might be the more suitable choice. 

Obviously, the decision depends on specific requirements, the scale of deployments and the features most important regards different kinds of projects/works.

## Documentation, Code and Presentation

In this repository, will be available: 

- Documentation where is explained and described the platform's architecture, including components, databases and their interactions, with a section on the security measures taken.
- Docker files and any code developed/modified for the cloud-based file storage system, with a README file with instructions on how to deploy and use the system developed.
- A short presentation summarizing the design and implementation.







