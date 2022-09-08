#!/usr/bin/bash

echo "Executing..."

python -m venv env

source env/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload