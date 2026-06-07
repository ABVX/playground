# Web Archiver Microservice

![CI](https://github.com/ABVX/playground/actions/workflows/main.yml/badge.svg)

Микросервис на Python для архивации веб-страниц с полным DevOps стеком.

## Стек
- **Python 3.9** + Flask
- **Docker** + Docker Compose
- **Kubernetes** — манифесты (Deployment, Service, Ingress)
- **Prometheus** + Grafana — мониторинг
- **Terraform** — инфраструктура как код
- **Ansible** — автоматизация
- **GitHub Actions** — CI/CD

## Быстрый старт
```bash
git clone https://github.com/ABVX/playground
cd playground
docker-compose -f docker/docker-compose.yml up -d
```

Сервис запустится на `http://localhost:8080`

## CI/CD
При каждом push в `main`:
1. Запускаются интеграционные тесты
2. Docker образ пушится в DockerHub

## Мониторинг
```bash
docker-compose -f docker-compose.monitoring.yml up -d
```
Prometheus: `http://localhost:9090`
Grafana: `http://localhost:3000`
