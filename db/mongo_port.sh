#!/bin/bash

export passwd=$MONGO_PASSWD
export db="myFirstDatabase"
export collect="Cusers" #maybe cuser_nm
export key="cuserName"

#python3 mongo_port.py $db $collect $key $passwd

#export collect="Busers"
#export key="busername"

python3 mongo_port.py $db $collect $key $passwd
