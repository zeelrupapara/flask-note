# Flask Note App
Application for taking notes

## Used Technologies:
- `Python`: 3.10
- `MariaDB`: 10.2
- `Flask`: 2.2.2


## Local Setup

#### First, create virtualenv if you want
```bash
python -m venv flask_note_env
```
###### Note: If you don't have venv than install it below way
```bash 
python -m pip install venv
```

#### After, craete virtualenv active this env 
```bash
. flask_note_env/bin/activate
```

#### After activation, need to install dependecies,
```bash
python -m pip install -r requirements.txt
```
#### Now set global env to run flask app
```bash
export FLASK_APP=main.py
export FLASK_ENV=development
```

#### Now, Run flask app,
`Recommend: Before run application apply migration`
```bash
flask run
```


### For, Apply Migration:
1. Create a migration repository

```python
flask db init
```

2. Create a migration script

```python
flask db migrate -m "init migration"
```

3. Apply the migration to the database

```python
flask db upgrade
```


## Run app with Docker
``` bash
docker compose up --build
```

See output 
https://localhost:5001
