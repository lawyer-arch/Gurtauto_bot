# GurtautoBot
Телеграм бот для приема заказов на покупку автомобилей в Телеграм.


Утсанавливаем виртуальное окружение:
```
python3 -m venv .venv
```

Устанавливаем poetry:
```
pip install poetry
```

Устанавливаем зависимости:
```
poetry install
```

Инициализация БД:
```
alembic revision --autogenerate -m "Initial migration"
```

Применяем миграцию:
```
alembic upgrade head
```
