#!/bin/bash
export FLASK_APP=caredash
#echo "Port: $1"
flask run --port $1
