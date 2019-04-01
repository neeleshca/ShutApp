#!/usr/bin/env bash

source ./env/bin/activate
export FLASK_APP=flaskr
export FLASK_ENV=development
flask init-db &
cd flaskr && rq worker save-image &
flask run & 
sleep 2 &
python3 flaskr/tests.py &
sleep 3
pkill -f flask -15
pkill -f "env/bin/rq worker save-image" -15
