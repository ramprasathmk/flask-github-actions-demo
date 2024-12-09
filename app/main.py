from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


@app.route('/')
def return_hello():
    return f"""
    <center><h1> Welcome </h1></center>
    <br/>
    <h3>Greetings</h3>
    """


@app.route('/<name>')
def return_hello_with_name(name: str = "Ramprasath M K"):
    return f"""
    <center><h1> Welcome </h1></center>
    <br/>
    <h3>Hi, {name}</h3>
    """


@app.route('/<random_string>')
def return_backwards_string(random_string):
    return "".join(reversed(random_string))


@app.route('/get-mode')
def get_mode():
    return os.environ.get("MODE")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
