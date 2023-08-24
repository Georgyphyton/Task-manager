install:
	poetry install

run:
	poetry run python3 manage.py runserver

migration:
	poetry run python3 manage.py makemigrations

migrate:
	poetry run python3 manage.py migrate

shell:
	poetry run python manage.py shell