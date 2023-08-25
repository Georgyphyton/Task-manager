MANAGE := poetry run python manage.py

install:
	poetry install

run:
	$(MANAGE) runserver

migration:
	$(MANAGE) makemigrations

omigrate:
	$(MANAGE) migrate

shell:
	$(MANAGE) shell

test:
	$(MANAGE) test

lint:
	poetry run flake8