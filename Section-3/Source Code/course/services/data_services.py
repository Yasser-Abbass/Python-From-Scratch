from mongoengine import *
from data.student import Student
from data.grade import Grade
from data.course import Course


def connect_to_db():
    db_rui = ""
    db_connection = connect(host=db_rui)


def create_student(firstname, lastname, email):
    student = Student(first_name=firstname, last_name=lastname, email=email)
    try:
        student.save()
        print('Student created successfully')
    except Exception as e:
        print(e)


def update_student(student, firstname, lastname, email):
    if firstname:
        fs = firstname
    else:
        fs = student.first_name
    if lastname:
        ls = lastname
    else:
        ls = student.last_name
    if email:
        em = email
    else:
        em = student.email
    student.first_name = fs
    student.last_name = ls
    student.email = em
    try:
        student.save()
        print('Student updated successfully')
    except Exception as e:
        print(e)


def delete_student(student):
    try:
        student.delete()
        print('Student deleted successfully')
    except Exception as e:
        print(e)


def get_student_by_email(email):
    student = Student.objects(email=email).first()

    return student


def get_student_by_name(firstname, lastname):
    student = Student.objects(Q(first_name=firstname) & Q(last_name=lastname)).first()

    return student


def student_add_degree(student, course, degree):
    grade = Grade(course=course, grade=degree)
    student.degree.append(grade)
    try:
        student.save()
        print('Grade added successfully')
    except Exception as e:
        print(e)


def create_course(name, max_students):
    course = Course(name=name, max_students=max_students)
    try:
        course.save()
        print('Course created successfully')
    except Exception as e:
        print(e)


def get_course(name):
    course = Course.objects(name=name).first()
    return course


def update_course(course, name, max_students):

    if name:
        cn = name
    else:
        cn = course.name
    if max_students:
        cm = max_students
    else:
        cm = course.max_students

    course.name = cn
    course.max_students = cm

    try:
        course.save()
        print('Course updated successfully')
    except Exception as e:
        print(e)


def delete_course(course):
    try:
        course.delete()
        print('Course deleted successfully')
    except Exception as e:
        print(e)


def list_courses():
    courses = Course.objects()
    for course in courses:
        print(f"Course {course.name} maximum students are {course.max_students}")


def add_student(course, student):
    course.students.append(student)
    try:
        course.save()
        print('Student added successfully')
    except Exception as e:
        print(e)


def add_grade(student, course, degree):
    grade = Grade(course=course, grade=degree)
    student.degree.append(grade)

    try:
        student.save()
        print('Grade added successfully')
    except Exception as e:
        print(e)
