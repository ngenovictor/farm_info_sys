#!/bin/sh

venv/bin/python manage.py migrate
# venv/bin/python manage.py collectstatic --noinput


if [ "$DEBUG" == "True" ]; then
    venv/bin/python manage.py runserver 0.0.0.0:8000
else
    venv/bin/python -m gunicorn farmisys.wsgi --bind 0.0.0.0:8000
fi
