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

echo ">>> [${BLUE}INFO${NC}]: EXECUTING $@."
exec "$@"