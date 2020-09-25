#! /usr/bin/env sh
set -e

DEFAULT_MODULE_NAME=backend.url_api.wsgi
VARIABLE_NAME=application
export APP_MODULE="$MODULE_NAME:$VARIABLE_NAME"

DEFAULT_GUNICORN_CONF=/backend/gunicorn_conf.py

export GUNICORN_CONF=${GUNICORN_CONF:-$DEFAULT_GUNICORN_CONF}
export WORKER_CLASS=${WORKER_CLASS:-"uvicorn.workers.UvicornWorker"}

PRE_START_PATH=${PRE_START_PATH:-/backend/prestart.sh}

echo "Running script $PRE_START_PATH"
. "$PRE_START_PATH"

exec gunicorn -k "$WORKER_CLASS" -c "$GUNICORN_CONF" "url_api.asgi:application"