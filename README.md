## Задание

Cделать конфигурацию docker-compose любого Вашего проекта из курса по Django, который использует БД (например, CRUD: Склады и запасы).

## Запуск приложения
Для запуска выполнить команды:

```docker-compose up -d --build```

```docker-compose run --rm backend sh -c "python manage.py migrate"```