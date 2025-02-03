migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

runserver:
	python manage.py runserver

initial_setup:
	python manage.py initial_setup data.json
