# ElectronicShopAPI

Это веб-приложение с API-интерфейсом представляет собой разработку онлайн платформы торговой сети электроники.
Сеть представляет собой иерархическую структуру из трех уровней:
завод;
розничная сеть;
индивидуальный предприниматель.
Каждое звено сети ссылается только на одного поставщика оборудования (не обязательно предыдущего по иерархии). 
Важно отметить, что уровень иерархии определяется не названием звена, а отношением к остальным элементам сети, 
завод всегда находится на уровне 0, а если розничная сеть относится напрямую к заводу, минуя остальные звенья, 
ее уровень — 1.

## Функционал

### Авторизация и аутентификация пользователей.
### CRUD для поставщиков.
### CRUD для продуктов.
### Распределение поставщиков по уровням при создании.


## Зависимости

Для управления зависимостями в проекте используется poetry.
Список зависимостей хранится в файле `pyproject.toml`
Установите все зависимости командой poetry install

## Установка

1. Клонируйте этот репозиторий на свой компьютер.
2. Установите необходимые зависимости с помощью `poetry install`.
3. Заполните файл `.env.example` и переименуйте его в `.env`.
4. Запустите проект командой `python manage.py runserver`.


## Запуск через docker compose
Сборка и запуск контейнера в фоновом режиме:
docker-compose up -d --build

## Документрация
Оформлена документация drf-yasg, ее можно просмотреть после запуска проекта:
http://localhost:8000/swagger или http://localhost:8000/redoc