start:
	poetry run watchmedo auto-restart --pattern="*.py" --recursive -- python main.py

initdb:
	python init_db.py

importdb:
	python import_cars.py