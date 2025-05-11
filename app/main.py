from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, template_folder="./templates")
PORT = os.getenv("PORT")


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def return_home():
    return render_template('index.html')


@app.route('/hello', methods=['GET'])
def return_hello():
    return render_template('hello.html')


@app.route('/hello/<name>', methods=['GET'])
def return_hello_with_name(name: str):
    return render_template('hello.html', name=name
                           )


@app.route('/random_string:<random_string>', methods=['GET', 'POST'])
def return_backwards_string(random_string):
    return "".join(reversed(random_string))


@app.route('/get-mode', methods=['GET'])
def get_mode():
    return os.environ.get("MODE")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=PORT)
