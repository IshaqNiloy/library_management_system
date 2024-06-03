run:
	python manage.py runserver 5000

migrate:
	python manage.py makemigrations
	python manage.py migrate

create-super-user:
	python manage.py createsuperuser
