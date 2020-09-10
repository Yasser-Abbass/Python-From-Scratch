from services import data_services


def print_main_menu():
    print("""
    please chose an option from the list
    [s] for student management
    [c] for course management
    [q] to quit the app
    """)


def print_student_menu():
    print("""
    please chose an option from the list
    [c] to create student
    [e] to find student by email
    [r] to find student by name
    [u] to update student
    [d] to delete student
    [s] to add student grade
    [x] quit to upper level menu
    """)
    return input('Please chose an option: ')


def print_course_menu():
    print("""
     please chose an option from the list
     [c] to create course
     [r] to find course
     [u] to update course
     [d] to delete course
     [l] to list all courses
     [s] to add student to course
     [x] quit to upper level menu
     """)
    return input('Please chose an option: ')


def create_student():
    firstname = input('Please enter student first name: ')
    lastname = input('Please enter student last name: ')
    email = input('Please enter student email: ')
    data_services.create_student(firstname=firstname, lastname=lastname, email=email)


def get_student_by_email():
    email = input('Please enter student email: ')
    student = data_services.get_student_by_email(email)
    print(f'Student with email {email} first name is {student.first_name} and last name is {student.last_name}')


def get_student_by_name():
    firstname = input('Please enter student first name: ')
    lastname = input('Please enter student last name: ')
    student = data_services.get_student_by_name(firstname=firstname, lastname=lastname)
    print(f'Student with first name {firstname} and last name {lastname} email is with email {student.email}')


def update_student():
    email = input('Please enter student email: ')
    student = data_services.get_student_by_email(email)
    firstname = input('Please enter student first name (Enter to skip): ')
    lastname = input('Please enter student last name (Enter to skip): ')
    email = input('Please enter student new email (Enter to skip): ')
    data_services.update_student(student, firstname, lastname, email)


def delete_student():
    email = input('Please enter student email: ')
    student = data_services.get_student_by_email(email)
    data_services.delete_student(student)


def add_grade_student():
    email = input('Please enter student email: ')
    student = data_services.get_student_by_email(email)
    crs = input('Please enter a course name: ')
    course = data_services.get_course(crs)
    degree = input('Please enter the grade: ')
    data_services.student_add_degree(student=student, course=course, degree=degree)


def create_course():
    name = input('Please enter course name: ')
    max_std = int(input('Please enter course max number of students: '))
    data_services.create_course(name=name, max_students=max_std)


def get_course():
    name = input('Please enter course name: ')
    course = data_services.get_course(name)
    print(f"Course {course.name} have maximum students of {course.max_students}")


def update_course():
    name = input('Please enter course name: ')
    crs = data_services.get_course(name)
    name = input('Please enter course name: ')
    max_std = int(input('Please enter course max number of students: '))
    data_services.update_course(crs, name, max_std)


def delete_course():
    name = input('Please enter course name: ')
    crs = data_services.get_course(name)
    data_services.delete_course(crs)


def list_courses():
    data_services.list_courses()


def add_student_course():
    name = input('Please enter course name: ')
    crs = data_services.get_course(name)
    email = input('Please enter student email: ')
    student = data_services.get_student_by_email(email)
    data_services.add_student(crs, student)


data_services.connect_to_db()


while True:
    print_main_menu()
    first_level_ip = input('Please chose an option: ')
    if first_level_ip == 's':

        while True:
            student_options = print_student_menu()
            if student_options == 'c':
                create_student()
            elif student_options == 'e':
                get_student_by_email()
            elif student_options == 'r':
                get_student_by_name()
            elif student_options == 'u':
                update_student()
            elif student_options == 'd':
                delete_student()
            elif student_options == 's':
                add_grade_student()
            elif student_options == 'x':
                break
            else:
                print('Please enter a valid option: ')
    elif first_level_ip == 'c':

        while True:
            course_options = print_course_menu()
            if course_options == 'c':
                create_course()
            elif course_options == 'r':
                get_course()
            elif course_options == 'u':
                update_course()
            elif course_options == 'd':
                delete_course()
            elif course_options == 'l':
                list_courses()
            elif course_options == 's':
                add_student_course()
            elif course_options == 'x':
                break
            else:
                print('Please enter a valid option: ')
    elif first_level_ip == 'q':
        quit()
    else:
        print('Please enter a valid option: ')