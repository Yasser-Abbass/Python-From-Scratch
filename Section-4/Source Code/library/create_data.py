import datetime

from data.book import Book
from data.borrow import Borrow
from data.publisher import Publisher
from data.subscriber import Subscriber
from services import data_services
from faker import Faker
import random


def create_subscribers(num):
    subscribers = []
    for i in range(num):
        subscriber = Subscriber()
        subscriber.first_name = fake.first_name()
        subscriber.last_name = fake.last_name()
        subscriber.email = fake.email()
        subscriber.address = fake.address()
        subscriber.ssn = fake.ssn()
        subscribers.append(subscriber)
    return subscribers


def create_publishers(num):
    publishers = []
    for i in range(num):
        publisher = Publisher()
        publisher.name = fake.name()
        publisher.founded = fake.date()
        publisher.location = fake.address()
        publishers.append(publisher)
    return publishers


def create_book(num):
    books = []
    publishers = Publisher.objects()
    subscribers = Subscriber.objects()
    for i in range(num):
        book = Book()
        book.title = fake.sentence(nb_words=4)
        book.author.append(fake.name())
        book.pages = fake.pyint(min_value=100, max_value=600)
        book.publish_date = fake.date()
        book.publisher = random.choices(publishers)[0]
        borrow = Borrow()
        borrow.subscriber = random.choices(subscribers)[0]
        borrow.start = fake.date_object()
        borrow.end = borrow.start + datetime.timedelta(days=random.randint(14, 60))
        book.borrowing_history.append(borrow)
        books.append(book)
    return books


fake = Faker()
data_services.connect_to_db()
subs = create_subscribers(100)
#Subscriber.objects.insert(subs)
pubs = create_publishers(100)
#Publisher.objects.insert(pubs)
books = create_book(100)
Book.objects.insert(books)
