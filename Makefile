
initdb:
	python init_db.py

migrate:
	alembic init migrations

init:
	alembic revision --autogenerate -m "init"
	alembic upgrade head
