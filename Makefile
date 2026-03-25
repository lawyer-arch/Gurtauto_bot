start:
	poetry run watchmedo auto-restart --pattern="*.py" --recursive -- python main.py

initdb:
	python init_db.py

migrate:
	alembic init migrations

init:
	alembic revision --autogenerate -m "init"
	alembic upgrade head