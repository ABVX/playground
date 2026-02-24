Мой Devops ROADMAP:

DevOps Roadmap
GIT

Learn one programming language

Learn Linux & Scripting

Learn Networking & Security

Learn Server Management

Learn Containers

Learn Container Orchestration

Learn Infrastructure as a Code (X as Code)

Learn CI/CD

Learn Monitoring & Observability

Learn one Cloud provider

Learn Software Engineering Practices

Bonus: Learn DevSecOps Fundamentals

22.02.2026 — Чему я научился
Bash & Автоматизация: Узнал разницу между while и until. Научился заменять "костыльный" sleep на динамическое ожидание файла (until [ -f index.html ]), что делает скрипты надежнее.

Git & GitHub:

Понял суть коммитов: это не просто сохранение, а описание изменений. Если в коммите с правкой run.sh написать про app.py, Гитхаб так и отобразит.

Научился использовать .gitattributes (linguist-vendored), чтобы "обманывать" статистику Гитхаба и скрывать ненужные языки (HTML), оставляя фокус на Shell и Docker.

Освоил git push --force для принудительной синхронизации веток.

Docker & Оркестрация:

Разобрался с порядком слоев в Dockerfile: сначала задаем WORKDIR, потом ставим зависимости, и только потом копируем код. Это база для быстрой сборки.

Понял, как связывать несколько контейнеров (Python + Nginx) через docker-compose.yml, пробрасывать порты и использовать volumes для связи файлов между ПК и контейнером.

Software Engineering: Начал практиковать атомарные коммиты — один файл за раз с четким описанием, чтобы история проекта была понятной.

24.02.26 - Чему я научился

Пофиксил синтаксическую ошибку в run.sh

Освоил команду docker exec -it, которая позволяет "проникать" внутрь запущенного контейнера и работать в его терминале.

Debug & File System:

Научился проверять содержимое контейнера с помощью ls -la.

Увидел на практике, как монтируются тома (volumes): файлы из моей папки на ПК мгновенно появляются внутри Nginx по пути /usr/share/nginx/html.

Права доступа (Permissions): Заметил, что файлы, созданные скриптом внутри контейнера, могут принадлежать root, в то время как файлы с хоста имеют другого владельца. Это важный нюанс для безопасности.
