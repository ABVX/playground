#EN
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
```bash
   git clone <link_to_your_repository>
   cd archiver

You should start service with this command:
docker-compose up

# RU
# Web Archiver Microservice

Простой микросервис на Python для архивации веб-страниц, полностью упакованный в Docker.

## Что делает этот проект?
* **Скачивает** HTML-код указанного URL.
* **Сохраняет** результат в файл `index.html`.
* **Изолирует** среду выполнения (Python, библиотеки) внутри контейнера.
* **Синхронизирует** полученные данные с локальной папкой через Docker Volumes.

## Технологии
* **Python 3.9** (библиотека `requests`)
* **Docker** (контейнеризация)
* **Docker Compose** (оркестрация запуска)
* **Git** (контроль версий)

## Как запустить
Убедитесь, что у вас установлены Docker и Docker Compose.

1. Склонируйте репозиторий:
   ```bash
   git clone <ссылка_на_твой_репозиторий>
   cd archiver
Запускайте сервис одной командой:
docker-compose up
