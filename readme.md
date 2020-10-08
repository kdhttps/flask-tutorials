# Flask Tutorials

## Configuration

1. `python3 -m venv venv` to setup virtual environment
1. `. venv/bin/activate` activate the environment
1. `pip3 install -r requirements.txt` install flask
1. `export FLASK_ENV=development` set it for auto reload and debugger

## Run

1. `export FLASK_APP=flasker` set `FLASK_APP` env
1. `flask run` run application

## others

1. How to create `requirements.txt` in fresh project
    
    ```python
    . venv/bin/activate
    pip3 freeze > requirements.txt
    ```

1. Install Deps in Fresh project

    ```
    pip3 install -r requirements.txt
    ```
