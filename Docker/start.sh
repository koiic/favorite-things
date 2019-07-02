#!/usr/bin/env bash

echo "=================================="
echo "=       RUNNING SERVER           ="
echo "=================================="
#Initialize database
flask db init

# Run database migrations
flask db migrate
flask db upgrade

# Run server

python manage.py runserver