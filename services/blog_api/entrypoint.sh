#!/bin/sh

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

if [ "$DATABASE" = "postgresql" ]
then
    echo ">>> [${BLUE}INFO${NC}]: WAITING FOR POSTGRESQL DATABASE."
    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done
    echo ">>> [${GREEN}SUCCESS${NC}]: POSTGRESQL DATABASE STARTED."
fi

if [ "$ENVIRONMENT" = "local" ]
then
    echo ">>> [${BLUE}INFO${NC}]: FLUSH DATABASE."
    python ./api/manage.py flush --noinput
    if [ $? -eq 0 ]
    then
        echo ">>> [${GREEN}SUCCESS${NC}]: DATABASE FLUSHED."
    else
        echo ">>> [${RED}ERROR${NC}]: FLUSHING DATABASE FAILED."
    fi

    echo ">>> [${BLUE}INFO${NC}]: DJANGO MAKEMIGRATIONS."
    python ./api/manage.py makemigrations
    if [ $? -eq 0 ]
    then
        echo ">>> [${GREEN}SUCCESS${NC}]: DJANGO MAKEMIGRATIONS COMPLETED."
    else
        echo ">>> [${RED}ERROR${NC}]: DJANGO MAKEMIGRATIONS FAILED."
    fi

    echo ">>> [${BLUE}INFO${NC}]: DJANGO MIGRATE."
    python ./api/manage.py migrate
    if [ $? -eq 0 ]
    then
        echo ">>> [${GREEN}SUCCESS${NC}]: DJANGO MIGRATE COMPLETED."
    else
        echo ">>> [${RED}ERROR${NC}]: DJANGO MIGRATE FAILED."
    fi

    echo ">>> [${BLUE}INFO${NC}]: CREATING DJANGO SUPERUSER."
    python ./api/manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL
    if [ $? -eq 0 ]
    then
        echo ">>> [${GREEN}SUCCESS${NC}]: DJANGO SUPERUSER CREATED."
    else
        echo ">>> [${RED}ERROR${NC}]: DJANGO CREATING SUPERUSER FAILED."
    fi

    echo ">>> [${BLUE}INFO${NC}]: LOAD FIXTURES INTO DATABASE."
    python ./api/manage.py loaddata ./api/blog/fixtures/db_fixtures.json
    if [ $? -eq 0 ]
    then
        echo ">>> [${GREEN}SUCCESS${NC}]: FIXTURES LOADED."
    else
        echo ">>> [${RED}ERROR${NC}]: LOADING FIXTURES FAILED."
    fi

    echo ">>> [${BLUE}INFO${NC}]: EXECUTING $@."
    exec "$@"
fi