from mongoengine import *

from data.book import Book
from data.borrow import Borrow
from data.publisher import Publisher
from data.subscriber import Subscriber
import os


def connect_to_db():
    db_uri = ''
    db_connection = connect(host=db_uri)
    return db_connection


def create_subscriber(firstname, lastname, email, address, ssn):
    subscriber = Subscriber()
    subscriber.first_name = firstname
    subscriber.last_name = lastname
    subscriber.email = email
    subscriber.address = address
    subscriber.ssn = ssn

    try:
        subscriber.save()
    except Exception as e:
        print(e)
    return subscriber


def update_subscriber(subs, firstname, lastname, email, address, ssn):
    subscriber = subs
    if firstname:
        fs = firstname
    else:
        fs = subscriber.first_name
    if lastname:
        ls = lastname
    else:
        ls = subscriber.last_name
    if email:
        em = email
    else:
        em = subscriber.email
    if address:
        add = address
    else:
        add = subscriber.address
    if ssn:
        ssn = ssn
    else:
        ssn = subscriber.ssn
    
    subscriber.first_name = fs
    subscriber.last_name = ls
    subscriber.email = em
    subscriber.address = add
    subscriber.ssn = ssn
    subscriber.save()
    return subscriber


def delete_subscriber(subs):
    subscriber = subs
    subscriber.delete()


def get_subscriber_by_email(email):
    subscriber = Subscriber.objects(email=email).first()

    return subscriber


def get_subscriber_by_name(firstname, lastname):
    subscriber = Subscriber.objects(Q(first_name=firstname) & Q(last_name=lastname)).first()

    return subscriber


def get_subscriber_by_ssn(ssn):
    subscriber = Subscriber.objects(ssn=ssn).first()

    return subscriber


def create_book(title, author, pages, publish_date, publisher):
    book = Book()
    book.title = title
    book.author.append(author)
    book.pages = pages
    if publish_date:
        book.publish_date = publish_date
    book.publisher = publisher
    book.save()
    return book


def update_book(bk, title, author, pages, publish_date, publisher):
    book = bk
    book.title = title
    book.author.append(author)
    book.pages = pages
    book.publish_date = publish_date
    book.publisher = publisher
    book.save()
    return book


def delete_book(bk):
    book = bk
    book.delete()


def get_book(bk):
    book = Book.objects(title=bk).first()
    return book


def book_add_subscriber(bk, subscriber, start, end):
    book = Book(bk)
    borrow = Borrow(subscriber=subscriber, start=start, end=end)
    book.borrowing_history.append(borrow)
    book.save()
    return book


def list_book():
    book = Book.objects()
    return book


def create_publisher(name, founded, location):
    publisher = Publisher(name=name, founded=founded, location=location).save()
    return publisher


def update_publisher(publisher, name, founded, location):
    publisher = publisher
    publisher.name = name
    publisher.founded = founded
    publisher.location = location
    publisher.save()
    return publisher


def delete_publisher(publisher):
    publisher = publisher
    publisher.delete()


def get_publisher(publisher):
    publisher = Publisher.objects(name=publisher).first()
    return publisher


def list_publisher():
    publisher = Publisher.objects()
    return publisher