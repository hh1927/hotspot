#!/bin/bash

export passwd=$MONGO_PASSWD
export db="cloud_DB"
export collect="Cusers"
export key="cuserName"

python3 mongo_port.py $db $collect $key $passwd
