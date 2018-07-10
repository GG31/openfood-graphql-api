# OpenFood graphql API
## Introduction
This project aims to give a graphql endpoint for the open food facts data

## Prerequisite
- python3
- python3-venv
- pip3
- pytest

## Getting started
Create your virtual environment
```
python3 -m venv venv
```
Activate the environment
```
. venv/bin/activate
```
Install dependencies
```
pip3 install -r requirements.txt
```
Set your database
```
mongorestore -d openfoodfacts -c products products.bson
```
Run
```
python3 main.py
```

## Testing
Run test
```
pytest -v -s
```

## Docker
```
docker build -t <project-name> .
docker run -it -p 5000 <project-name>
```
Then go to `http://0.0.0.0:5000`

