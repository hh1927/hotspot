#!/bin/bash

HOST=127.0.0.1
PORT=8000

export HOTSPOT_HOME = /home/runner/work/hotspot/hotspot/API
if [ $ANUBIS ]
then
    HOST=0.0.0.0
fi

# run our server locally:
PYTHONPATH=$(pwd):$PYTHONPATH
FLASK_APP=endpoints flask run --host=127.0.0.1 --port=8000
