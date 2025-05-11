# flask-github-actions-demo

[![CI](https://github.com/ramprasathmk/flask-github-actions-demo/actions/workflows/flask_test.yml/badge.svg)](https://github.com/ramprasathmk/flask-github-actions-demo/actions/workflows/flask_test.yml)


## Description

- The simple flask app built on the `uv`(python project management tool).

## Basic Requirements

- Pycharm (latest)  or 
- VSCode (latest)
- Python >= `3.7`
- Pip (latest)
- Flask (latest)
- UV (latest)

## Commands Used for the 

- The installation of **uv** package:
  - ```python -m pip install uv```
  - ```uv --version```

- The project creation:
  - Select any workspace to create the sample project
  - Go to the workspace and then 
    - ```uv init webapp```
  - Create the Python Virtual Environment 
    - ```uv venv .venv```
  - Install the necessary packages for your project
    - ```uv add <package1> <package2> ...``` or
    - ```uv pip install <package_name>```
  - Run the webapp
    - ```uv run main.py```
