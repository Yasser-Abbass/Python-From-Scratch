from data.course import Course
from data.grade import Grade
from services import data_services
from faker import Faker
import random
import datetime
from data.student import Student


fake = Faker()
Faker.seed(1234)
start_time = datetime.datetime.now()
data_services.connect_to_db()

students = []
for i in range(1000):
    firstname = fake.first_name()
    lastname = fake.last_name()
    email = fake.email()
    student = Student(first_name=firstname, last_name=lastname, email=email)
    students.append(student)

#Student.objects.insert(students)
print(f"{datetime.datetime.now() - start_time} seconds had passed")

start_time = datetime.datetime.now()
crs = []
courses = ['History', 'Math', 'Science', 'Biology', 'French']
for name in courses:
    course = Course()
    course.name = name
    course.max_students = fake.pyint(max_value=40, min_value=10)
    crs.append(course)

#Course.objects.insert(crs)
print(f"{datetime.datetime.now() - start_time} seconds had passed")

start_time = datetime.datetime.now()
students = Student.objects()
courses = Course.objects()
# for course in courses:
#     course.students = random.choices(students, k=course.max_students)
#     course.save()

print(f"{datetime.datetime.now() - start_time} seconds had passed")

start_time = datetime.datetime.now()
for course in courses:
    for student in course.students:
        grade = Grade(course=course, grade=fake.pyfloat(min_value=50, max_value=95))
        student.degree.append(grade)
        student.save()

print(f"{datetime.datetime.now() - start_time} seconds had passed")