from services import data_services
import datetime


def print_main_menu():
    print('''
    please chose an option from below
    [s] for subscriber management
    [b] for books management
    [p] for publisher management
    [q] to quit the software
    ''')

    return input("Please select an option to begin the process ? ")


def print_subscriber_menu():
    print('''
    [c] to create subscriber
    [e] to find subscriber by email
    [r] to find subscriber by name
    [s] to find subscriber by ssn
    [u] to update subscriber
    [d] to delete subscriber
    [x] for upper level menu
    ''')
    return input("Please select an option to begin the process ? ")


def print_book_menu():
    print('''
    [c] to create book
    [u] to update book
    [d] to delete book
    [r] to find book
    [l] to list all books
    [s] to borrow book 
    [x] for upper level menu
    ''')
    return input("Please select an option to begin the process ? ")


def print_publisher_menu():
    print('''
    [c] to create publisher
    [u] to update publisher
    [d] to delete publisher
    [r] to find publisher
    [l] to list all publishers
    [x] for upper level menu
    ''')
    return input("Please select an option to begin the process ? ")


def create_subscriber():
    fist_name = input('Please Enter subscriber first name: ')
    last_name = input('Please Enter subscriber last name: ')
    email = input('Please Enter subscriber email: ')
    address = input('Please Enter subscriber address: ')
    ssn = input('Please Enter subscriber ssn: ')

    subscriber = data_services.create_subscriber(firstname=fist_name, lastname=last_name, email=email,
                                                 address=address, ssn=ssn)
    if subscriber:
        print('Student created successfully')
    else:
        print("Unable to create subscriber")


def get_subscribers_books(subscriber):
    pass


def find_subscriber_by_mail():
    email = input('Please Enter subscriber email: ')
    std = data_services.get_subscriber_by_email(email=email)
    print(f'subscriber with email {std.email} first name is {std.first_name} and last name is {std.last_name}')
    get_subscribers_books(std)


def find_subscriber_by_name():
    fist_name = input('Please Enter subscriber first name: ')
    last_name = input('Please Enter subscriber last name: ')
    std = data_services.get_subscriber_by_name(firstname=fist_name, lastname=last_name)
    print(f'subscriber with email {std.email} first name is {std.first_name} and last name is {std.last_name}')
    get_subscribers_books(std)


def update_subscriber():
    email = input('Please Enter subscriber email: ')
    std = data_services.get_subscriber_by_email(email=email)
    fist_name = input('Please Enter subscriber first name: ')
    last_name = input('Please Enter subscriber last name: ')
    email = input('Please Enter subscriber email: ')
    address = input('Please Enter subscriber address: ')
    ssn = input('Please Enter subscriber ssn: ')
    std2 = data_services.update_subscriber(subs=std, firstname=fist_name, lastname=last_name, email=email,
                                           address=address, ssn=ssn)
    print(f'subscriber with email {std2.email} first name is {std2.first_name} and last name is {std2.last_name}')


def delete_subscriber():
    email = input('Please Enter subscriber email: ')
    std = data_services.get_subscriber_by_email(email=email)
    data_services.delete_subscriber(std=std)
    print(f'subscriber deleted successfully')


def create_book():
    title = input('Please Enter book name: ')
    author = input('Please Enter book author: ')
    pages = input('Please Enter book pages: ')
    publish_date = input('Please Enter publish date (default is today: ')
    publisher = input('Please Enter publisher name: ')
    publisher = data_services.get_publisher(publisher)
    book = data_services.create_book(title=title, author=author, pages=pages, publish_date=publish_date,
                                     publisher=publisher)
    if book:
        print('Book created successfully')
    else:
        print("Unable to create book")


def find_book():
    bk = input('Please Enter book name: ')
    book = data_services.get_book(bk=bk)
    if book:
        print(f"Book {book.title} author {book.author} number of pages {book.pages}")
        print('The following subscribers had borrowed this book:')
        for std in book.borrowing_history:
            print(f'Subscriber {std.first_name} {std.last_name}')


def update_book():
    title = input('Please Enter book name: ')
    book = data_services.get_book(bk=title)
    title = input('Please Enter book name: ')
    author = input('Please Enter book author: ')
    pages = input('Please Enter book pages: ')
    publish_date = input('Please Enter publish date (default is today: ')
    publisher = input('Please Enter publisher name: ')
    publisher = data_services.get_publisher(publisher)
    data_services.update_book(bk=book, title=title, author=author, pages=pages, publish_date=publish_date,
                              publisher=publisher)


def delete_book():
    title = input('Please Enter book name: ')
    book = data_services.get_book(bk=title)
    data_services.delete_book(bk=book)
    print(f'Book deleted successfully')


def list_books():
    books = data_services.list_book()
    for book in books:
        print(f'Book {book.title} author {book.author}')


def borrow_book():
    email = input('Please Enter subscriber email: ')
    subscriber = data_services.get_subscriber_by_email(email=email)
    book = input('Please enter book name: ')
    book = data_services.get_book(bk=book)
    start = input('Please enter book borrow date (dd/mm/yy): ')
    end = input('Please enter how many days you will borrow the book ')
    start_date = datetime.datetime.strptime(start, format="%d/%m/%y")
    end_date = start_date + datetime.timedelta(days=int(end))
    data_services.book_add_subscriber(bk=book, subscriber=subscriber, start=start_date, end=end_date)


def create_publisher():
    name = input('Please Enter publisher name: ')
    founded = input('Please Enter publisher founded: ')
    location = input('Please Enter publisher location: ')
    publisher = data_services.create_publisher(name=name, founded=founded, location=location)
    if publisher:
        print('Publisher created successfully')
    else:
        print("Unable to create Publisher")


def find_publisher():
    name = input('Please Enter publisher name: ')
    publisher = data_services.get_publisher(publisher=name)
    print(f"Publisher {publisher.name} founded in {publisher.founded} and located in  {publisher.location}")


def update_publisher():
    name = input('Please Enter publisher name: ')
    publisher = data_services.get_publisher(publisher=name)
    name = input('Please Enter publisher name: ')
    founded = input('Please Enter publisher founded: ')
    location = input('Please Enter publisher location: ')
    data_services.update_publisher(publisher=publisher, name=name, founded=founded, location=location)


def delete_publisher():
    name = input('Please Enter publisher name: ')
    publisher = data_services.get_publisher(publisher=name)
    data_services.delete_publisher(publisher=publisher)
    print(f'Publisher deleted successfully')


def list_publisher():
    publisher = data_services.list_publisher()
    for pub in publisher:
        print(f"Publisher {pub.name} founded in {pub.founded} and located in  {pub.location}")

print('''
    
    ooooooooooooooooooooooooooooooooooooooooooooooooooooooo
    o                                                     o
    o                                                     o
    o                                                     o
    o      Welcome to Library XYZ Borrowing services      o
    o                                                     o
    o                                                     o
    o                                                     o
    oooooooooooooooooooooooooooooooooooooooooooooooooooooooo
''')
data_services.connect_to_db()

while True:
    first_level_menu = print_main_menu()
    if first_level_menu == 's':
        while True:
            second_level_menu = print_subscriber_menu()
            if second_level_menu == 'c':
                create_subscriber()
            elif second_level_menu == 'e':
                find_subscriber_by_mail()
            elif second_level_menu == 'r':
                find_subscriber_by_name()
            elif second_level_menu == 'u':
                update_subscriber()
            elif second_level_menu == 'd':
                delete_subscriber()
            elif second_level_menu == 'x':
                break
            else:
                print('Please choose a valid option')
    elif first_level_menu == 'b':
        while True:
            third_level_menu = print_book_menu()
            if third_level_menu == 'c':
                create_book()
            elif third_level_menu == 'r':
                find_book()
            elif third_level_menu == 'u':
                update_book()
            elif third_level_menu == 'd':
                delete_book()
            elif third_level_menu == 'l':
                list_books()
            elif third_level_menu == 's':
                borrow_book()
            elif third_level_menu == 'x':
                break
            else:
                print('Please choose a valid option')
    elif first_level_menu == 'p':
        while True:
            third_level_menu = print_publisher_menu()
            if third_level_menu == 'c':
                create_publisher()
            elif third_level_menu == 'r':
                find_publisher()
            elif third_level_menu == 'u':
                update_publisher()
            elif third_level_menu == 'd':
                delete_publisher()
            elif third_level_menu == 'l':
                list_publisher()
            elif third_level_menu == 'x':
                break
            else:
                print('Please choose a valid option')

    elif first_level_menu == 'q':
        quit()
    else:
        print('Please choose a valid option')
