#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py compress --force

gunicorn core.wsgi:application -c /etc/gunicorn/gunicorn.conf.py