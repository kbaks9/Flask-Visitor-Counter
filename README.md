# Docker Challenge: Flask Application with Redis

This repository contains a lightweight Flask-based web application that records and displays page visit counts using Redis as its backend data store. The application is fully containerised using Docker and Docker Compose, allowing for consistent environments, simple setup, and reproducible builds.

The root endpoint presents a welcome page, while a separate endpoint is responsible for incrementing and showing the total number of visits.

Visitor counter preview:
https://github.com/user-attachments/assets/d96a6ab5-aaa4-45e1-9d15-f4c6ec769a13

---

## FEATURES

- Homepage (`/`) displaying a welcome message
- Visitor counter endpoint (`/count`) backed by Redis
- Persistent Redis data using Docker volumes
- Custom CSS styling
- Multi-container setup managed by Docker Compose
- Environment-based configuration
- Scalable design with planned Nginx load balancing

---

## REQUIREMENTS

- Docker
- Docker Compose (v2 recommended)

---

## RUNNING THE APPLICATION

Clone the repository and start the application with:

docker compose up --scale web=3 --build

Once the containers are running, access the application:

Application: http://localhost:5002  
Visitor Counter: http://localhost:5002/count

---

## SCALING THE WEB SERVICE

The Flask web service can be scaled horizontally using Docker Compose:

docker compose up --scale web=3

Note:  
When running multiple Flask containers, a reverse proxy such as Nginx is required to properly load-balance traffic. Nginx integration is planned for a future update.

---

## ENVIRONMENT VARIABLES

The application uses the following environment variables:

- REDIS_HOST – Redis service hostname (default: redis)
- REDIS_PORT – Redis port (default: 5002)

These values are automatically defined in the docker-compose.yaml file.

---

## STOPPING THE APPLICATION

To stop and remove all containers, networks, and volumes:

docker compose down

---

## PROJECT STRUCTURE

├── app.py  
├── Dockerfile  
├── docker-compose.yaml  
├── nginx.conf  
├── images/  
│   └── counter.gif  
├── static/  
│   └── style.css  
├── templates/  
│   ├── home.html  
│   └── count.html  
└── README.md  

---

## PLANNED IMPROVEMENTS

- Add Nginx reverse proxy for load balancing
- Implement health checks and monitoring

---

## LICENSE

This project is intended for learning and demonstration purposes only.
