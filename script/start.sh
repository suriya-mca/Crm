#!/bin/sh

python manage.py makemigrations
python manage.py migrate

# collects all static files in our app and puts it in the STATIC_ROOT
python manage.py collectstatic --noinput

gunicorn core.wsgi:application -c /etc/gunicorn/gunicorn.conf.py