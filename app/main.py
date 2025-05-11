from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()

app:Flask = Flask(__name__, template_folder="./templates")
PORT:str = os.getenv("PORT")


@app.route('/')
@app.route('/home')
def return_home():
    return render_template('index.html')


@app.route('/hello')
def return_hello():
    return render_template('hello.html')


@app.route('/hello/<name>')
def return_hello_with_name(name: str):
    return render_template('hello.html', name=name
                           )


@app.route('/random_string:<random_string>')
def return_backwards_string(random_string):
    return "".join(reversed(random_string))


@app.route('/get-mode')
def get_mode():
    return os.environ.get("MODE")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=PORT)
