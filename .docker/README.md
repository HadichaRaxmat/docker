# Название проекта: FastAPI и PostgreSQL с Docker

## Описание
Этот проект представляет собой приложение с использованием FastAPI для создания веб-сервиса и PostgreSQL для хранения данных. Также настроен Swagger UI для тестирования API.

Проект использует Docker для контейнеризации, включая контейнеры для FastAPI-приложения, PostgreSQL и Swagger UI.

## Стек технологий
- **FastAPI** — современный веб-фреймворк для создания API.
- **PostgreSQL** — реляционная база данных.
- **Docker** — инструмент для создания контейнеров и упрощения развёртывания.
- **Swagger UI** — интерфейс для тестирования API.

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/HadichaRaxmat/docker.git
    ```

2. Перейдите в директорию проекта:
    ```bash
    cd ваш_проект
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Запуск приложения

1. Запустите контейнеры с помощью Docker Compose:
    ```bash
    docker-compose up --build
    ```

2. Приложение будет доступно по следующим адресам:
    - FastAPI: `http://localhost:8100/docs` (Swagger UI)
    - HTTP-сервер: `http://localhost:8000`
    - pgadmin4 BD: `http://localhost:8080`

## Структура проекта

- `Dockerfile`: описание для сборки контейнера с FastAPI.
- `docker-compose.yml`: конфигурация для запуска нескольких контейнеров (FastAPI, PostgreSQL, Swagger).
- `app.py`: код FastAPI-приложения с CRUD для базы данных.
- `requirements.txt`: список зависимостей для Python.

