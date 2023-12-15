#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! pg_isready -h $DATABASE_HOST -p $DATABASE_PORT -q -U $DATABASE_USER; do
      sleep 1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate

exec "$@"