#!/bin/bash

export passwd=$MONGO_PASSWD
export db="hotspot"
export collect="business"
export key="business_name"
export collect="consumer"
export key="username"
export collect="events"
export key="event_name"

python3 mongo_port.py $db $collect $key $passwd
