from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    name = ['Tim', 'John', 'Jack', 'Marry']
    return render_template('index2.html', students=name, title='Home')


@app.route('/hi/<name>')
def hi(name):
    return f'Hello {name}'


if __name__ == "__main__":
    app.run(debug=True)