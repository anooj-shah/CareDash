#!/bin/bash
export FLASK_APP=caredash
pip install flask_sqlalchemy
pip install Flask
python3 setup.py
#echo "Port: $1"
flask run --port $1
