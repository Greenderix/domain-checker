# Domain-checker
## Веб-сервис для отслеживания посещенных веб-ресурсов

Сохраняет список посещенных URL-адресов в базу данных.

## Описание

### Технологический стек:
- Python 3.10
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- Pytest

Документация API доступна через [Swagger](localhost:8000/docs).

## Запуск
1. ### Клонировать проект
```
git clone https://github.com/Greenderix/domain-checker.git
```
2. Перейдите в корневую папку проекта.
3. В терминале введите команду ```docker compose up --build```.

**Примечание:** Убедитесь, что у вас установлен и запущен Docker Desktop последней версии.

**Примечание:** Файл `.env` с базовыми настройками должен присутствовать в проекте.

После выполнения команды начнется сборка контейнеров для базы данных (PostgreSQL) и приложения. Дождитесь окончания процесса сборки. Приложение будет доступно по адресу [localhost:8000/docs](localhost:8000/docs).

## Запуск тестов
### Предустановленное:

- Python 3
### Создать виртуальное окружение **Если не создано**

```
python 3 -m venv venv
```
### Запустить виртуальное окружение на MacOS/Linux

```
source venv/bin/activate
```
### Запустить виртуальное окружение на Windows

```
venv/Scripts/activate
```

### Выполнить следующие пункты:

1. Убедитесь, что запущен Docker-контейнер проекта.
2. Введите команду ```pytest test.py```.

#### Вы также можете проверить тестовые значения, которые подгружаются сразу при развертке проекта.
from_time=1545221231
to_time=1545255555
  ```http://localhost:8000/visited_domains?from_time=1545221231&to_time=1545255555```
