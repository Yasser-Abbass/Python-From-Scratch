from flask import Flask, render_template, redirect, request, flash
from flask_mongoengine import MongoEngine
from faker import Faker
from subscriber import Subscriber
from forms import SubscriberForm
import os


app = Flask(__name__, static_folder='templates/assets')
uri = ""
app.config['MONGODB_SETTINGS'] = {
    'db': "Subscribers",
    'host': uri
}
app.config['SECRET_KEY'] = "57713873151f79143bc992f157398c46"

db = MongoEngine(app)
fake = Faker()


def create_subscribers(num):
    subscribers = []
    for i in range(num):
        subscriber = Subscriber()
        subscriber.name = fake.name()
        subscriber.phone = fake.phone_number()
        subscriber.email = fake.email()
        subscriber.address = fake.address()
        subscribers.append(subscriber)
    Subscriber.objects.insert(subscribers)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/list')
def list_subscribers():
    page = request.args.get('page', 1, type=int)
    subscribers = Subscriber.objects.order_by('name').paginate(page=page, per_page=25)
    return render_template('list_subscriber.html', subscribers=subscribers, pages=subscribers)


@app.route('/new', methods=['GET', 'POST'])
def create_subscriber():
    form = SubscriberForm()
    if request.method == 'GET':
        return render_template('subscriber.html', form=form)
    elif request.method == 'POST':
        if form.submit.data:
            if form.validate_on_submit():
                subscriber = Subscriber()
                subscriber.name = form.name.data
                subscriber.email = form.email.data
                subscriber.phone = form.phone.data
                subscriber.address = form.address.data
                subscriber.save()
                flash("Subscriber created successfully", 'success')
        return redirect('/list')


@app.route("/delete/<id>")
def delete_subscriber(id):
    subscriber = Subscriber.objects(id=id).first()
    subscriber.delete()
    flash("Subscriber deleted successfully", 'success')
    return redirect("/list")


@app.route("/edit/<id>", methods=['GET', 'POST'])
def edit_subscriber(id):
    subscriber = Subscriber.objects(id=id).first()
    form = SubscriberForm(obj=subscriber)
    if request.method == 'GET':
        return render_template('subscriber.html', form=form, id=id)
    elif request.method == 'POST':
        if form.submit.data:
            if form.validate_on_submit():
                subscriber.name = form.name.data
                subscriber.email = form.email.data
                subscriber.phone = form.phone.data
                subscriber.address = form.address.data
                subscriber.save()
                flash("Subscriber created successfully", 'success')
        return redirect("/list")


if __name__ == "__main__":
    #create_subscribers(1000)
    app.run(debug=True)

