from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, static_folder='templates/assets')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/products')
def hi():
    names = ['Tim', 'Tom', 'Jack', 'Marry', 'Carl']
    return render_template('products.html', names=names)


if __name__ == "__main__":
    app.run(debug=True)