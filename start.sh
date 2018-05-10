#!/bin/sh
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py carrot_daemon start
/usr/local/bin/gunicorn web.wsgi:application -w 2 -b :8000
exec "$@"
