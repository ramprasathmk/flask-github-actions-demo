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
  - ```bash
    python -m pip install uv
    ```
  - ```bash
    uv --version
    ```

- The project creation:
  - Select any workspace to create the sample flask project
  - Go to the workspace and then 
    - ```bash 
      uv init webapp
      ```
  - Create the Python Virtual Environment 
    - ```bash 
      uv venv .venv
      ```
  - Install the necessary packages for your project
    - ```bash 
      uv add <package1> <package2> ...
      ``` 
      or
    - ```bash 
      uv pip install <package_name>
      ```
  - Run the webapp
    - ```bash 
      uv run app/main.py
      ```
