start:
	poetry run watchmedo auto-restart --pattern="*.py" --recursive -- python main.py