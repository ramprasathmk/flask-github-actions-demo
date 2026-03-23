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

## Installation

  - Clone this git repository
    ```bash
    > git clone https://github.com/ramprasathmk/flask-github-actions-demo.git
    ```
    
  - Change current working directory
    ```bash
    > cd flask-github-actions-demo
    ```
    
  - Install python package manager
    ```bash
    python -m pip install uv
    ```
    
  - Check it works properly
    ```bash
    uv --version
    ```

  - Create Python Virtual Environment
    ```bash
    uv venv .venv
    ```
  
  - Activate Virtual Environment
    ```bash
    > & .venv/Scripts/activate
    ```

  - Install python packages
    ```bash
    uv pip install -r repuirements.txt
    ```

  - Run the application
    ```bash
    uv run app/main.py
    ```

## The project creation (only for new projects):
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
