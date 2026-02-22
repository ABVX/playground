# Web Archiver Microservice

A simple Python microservice for archiving web pages, fully packaged in Docker.

## What does this project do?
* **Downloads** the HTML code of the specified URL.
* **Saves** the result to the `index.html` file.
* **Isolates** the execution environment (Python, libraries) inside the container.
* **Synchronizes** the received data with the local folder via Docker Volumes.

## Technologies
* **Python 3.9** (`requests` library)
* **Docker** (containerization)
* **Docker Compose** (launch orchestration)
* **Git** (version control)

## How to run
Make sure you have Docker and Docker Compose installed.

1. Clone the repository:
   git clone <link_to_your_repository>
   cd archiver

You should start service with this command:
docker-compose up


