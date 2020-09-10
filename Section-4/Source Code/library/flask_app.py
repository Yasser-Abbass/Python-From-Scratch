from flask import Flask, render_template, redirect, request, flash
from flask_mongoengine import MongoEngine

from forms import PublisherForm, BookForm, SubscriberForm
from services import data_services
from faker import Faker
import os


app = Flask(__name__, static_folder='templates/assets')
uri = "mongodb+srv://yasso:"+os.environ.get("MONGO_PASS")+"@cluster0.hkhqb.mongodb.net/Library?retryWrites=true&w=majority"
app.config['MONGODB_SETTINGS'] = {
    'db': "Library",
    'host': uri
}
app.config['SECRET_KEY'] = "57713873151f79143bc992f157398c46"

db = MongoEngine(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/publisher/list')
def list_publishers():
    page = request.args.get('page', 1, type=int)
    publisher = data_services.list_publisher(page=page, per_page=10)
    return render_template('publisher_list.html', publishers=publisher, pages=publisher)


@app.route('/publisher/new', methods=['GET', 'POST'])
def new_publisher():
    form = PublisherForm()
    if request.method == "GET":
        return render_template('edit_publisher.html', form=form, status='new')
    elif request.method == 'POST':
        if form.validate_on_submit():
            data_services.create_publisher(name=form.name.data,
                                           founded=form.founded.data,
                                           location=form.location.data)
            flash('Publisher created successfully', 'success')
        else:
            for k, v in form.errors.items():
                flash(v[0], 'danger')
            return render_template('edit_publisher.html', form=form, status='new')

        return redirect('/publisher/list')


@app.route('/publisher/edit/<id>', methods=['GET', 'POST'])
def edit_publisher(id):
    form = PublisherForm()
    publisher = data_services.get_publisher(id)
    if request.method == "GET":
        form = PublisherForm(obj=publisher)
        return render_template('edit_publisher.html', form=form, status='edit')
    elif request.method == 'POST':
        if form.update.data:
            if form.validate_on_submit():
                data_services.update_publisher(publisher=publisher,
                                               name=form.name.data,
                                               founded=form.founded.data,
                                               location=form.location.data)
                flash('Publisher created successfully', 'success')
            else:
                for k, v in form.errors.items():
                    flash(v[0], 'danger')
                return render_template('edit_publisher.html', form=form, status='edit')
        elif form.delete.data:
            data_services.delete_publisher(publisher=publisher)
            flash('Publisher deleted successfully', 'success')
        return redirect('/publisher/list')


@app.route('/subscriber/list')
def list_subscriber():
    page = request.args.get('page', 1, type=int)
    subscriber = data_services.list_subscriber(page=page, per_page=10)
    return render_template('subscriber_list.html', subscribers=subscriber, pages=subscriber)


@app.route('/subscriber/new', methods=['GET', 'POST'])
def new_subscriber():
    form = SubscriberForm()
    if request.method == 'GET':
        return render_template('edit_subscriber.html', form=form, status='new')
    elif request.method == 'POST':
        if form.validate_on_submit():
            data_services.create_subscriber(firstname=form.first_name.data,
                                            lastname=form.last_name.data,
                                            email=form.email.data,
                                            address=form.address.data,
                                            ssn=form.ssn.data)
            flash('Subscriber created successfully', 'success')
        else:
            for k, v in form.errors.items():
                flash(v[0], 'danger')
            return render_template('edit_subscriber.html', form=form, status='new')
        return redirect('/subscriber/list')


@app.route('/subscriber/edit/<id>', methods=['GET', 'POST'])
def edit_subscriber(id):
    form = SubscriberForm()
    subscriber = data_services.get_subscriber_by_id(id)
    if request.method == "GET":
        form = SubscriberForm(obj=subscriber)
        return render_template('edit_subscriber.html', form=form, status='edit')
    elif request.method == 'POST':
        if form.update.data:
            if form.validate_on_submit():
                data_services.update_subscriber(subs=subscriber,
                                                firstname=form.first_name.data,
                                                lastname=form.last_name.data,
                                                email=form.email.data,
                                                address=form.address.data,
                                                ssn=form.ssn.data)
                flash('Subscriber created successfully', 'success')
            else:
                for k, v in form.errors.items():
                    flash(v[0], 'danger')
                return render_template('edit_subscriber.html', form=form, status='edit')
        elif form.delete.data:
            data_services.delete_subscriber(subs=subscriber)
            flash('Subscriber deleted successfully', 'success')
        return redirect('/subscriber/list')


@app.route('/book/list')
def list_book():
    page = request.args.get('page', 1, type=int)
    books = data_services.list_book(page=page, per_page=10)
    return render_template('book_list.html', books=books, pages=books)


@app.route('/book/new', methods=['GET', 'POST'])
def new_book():
    form = BookForm()
    if request.method == 'GET':
        publishers = data_services.get_all_publishers()
        form.publisher.choices = [(publisher.id, publisher.name) for publisher in publishers]
        return render_template('edit_book.html', form=form, status='new')
    elif request.method == 'POST':
        if form.validate_on_submit():
            publisher = data_services.get_publisher(form.publisher.data)
            data_services.create_book(title=form.title.data,
                                      author=form.author.data,
                                      pages=form.pages.data,
                                      publish_date=form.publish_date.data,
                                      publisher=publisher)
            flash('Book created successfully', 'success')
        else:
            for k, v in form.errors.items():
                flash(v[0], 'danger')
            return render_template('edit_book.html', form=form, status='new')
        return redirect('/book/list')


@app.route('/book/edit/<id>', methods=['GET', 'POST'])
def edit_book(id):
    form = BookForm()
    book = data_services.get_book_by_id(id)
    if request.method == 'GET':
        authors = ""
        for author in book.author:
            authors = author + ", "
        form = BookForm(obj=book)
        form.author.data = authors
        subscribers = data_services.get_all_subscriber()
        form.subscriber.choices = [(subscriber.id, subscriber.email) for subscriber in subscribers]
        form.subscriber.process_data(subscribers[0].id)
        publishers = data_services.get_all_publishers()
        form.publisher.choices = [(publisher.id, publisher.name) for publisher in publishers]
        form.publisher.process_data(book.publisher.id)
        return render_template('edit_book.html', form=form, status='edit')
    elif request.method == 'POST':
        if form.update.data:
            if form.validate_on_submit():
                authors = []
                for a in form.author.data.split(","):
                    if a != "" and a != " ":
                        authors.append(a)
                publisher = data_services.get_publisher(form.publisher.data)
                data_services.update_book(bk=book,
                                          title=form.title.data,
                                          author=form.author.data,
                                          pages=form.pages.data,
                                          publish_date=form.publish_date.data,
                                          publisher=publisher)
                flash('Book created successfully', 'success')
            else:
                for k, v in form.errors.items():
                    flash(v[0], 'danger')
                return render_template('edit_book.html', form=form, status='edit')
        elif form.delete.data:
            data_services.delete_book(book)
            flash('Book deleted successfully', 'success')
        elif form.borrow.data:
            subscriber = data_services.get_subscriber_by_id(form.subscriber.data)
            data_services.book_add_subscriber(bk=book,
                                              subscriber=subscriber,
                                              start=form.start.data,
                                              end=form.end.data)
            flash('Book borrow created successfully', 'success')
        return redirect('/book/list')


if __name__ == "__main__":
    app.run(debug=True)
