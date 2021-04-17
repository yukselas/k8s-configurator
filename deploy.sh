#!/bin/bash

sudo apt install -y python3 python3-pip
pip3 install -r requirements.txt
export FLASK_APP=app
python3 -m flask run --host=0.0.0.0
