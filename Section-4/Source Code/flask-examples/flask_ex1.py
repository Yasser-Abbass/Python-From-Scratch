from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World'


@app.route('/hi/<name>')
def hi(name):
    return f"Hi {name}"


if __name__ == "__main__":
    app.run(debug=True)