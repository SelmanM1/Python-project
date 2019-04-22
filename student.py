
import os
import platform
import csv
import time
from prettytable import from_csv
import header_design as design
import main
import preloader
from student_details import Student_Details
from person import Student
tab = '\t'
operating_system = platform.system()


def id_generator():
    id_list = []
    default_student_id = 1001
    try:
        with open('student_database.csv', 'r') as fr:
            data = csv.reader(fr)
            for student_id in data:
                id_list.append(student_id[0])
            student_id = int(id_list[-1]) + 1
            return student_id
    except Exception:
        return default_student_id


# Adding New Student
def student_input():
  #  Student_Details.student_info(operating_system)
    info=Student.get_user_input(operating_system)
    firstname=info['first_name']
    middlename=info['middle_name']
    lastname=info['last_name']
    age=info['age']
    gender=info['gender']
    department=info['department']
    course=info['course']
    new_student= Student(firstname,middlename,lastname,age,gender,department,course)
    new_student.save_student_info(operating_system)
   
# Show student database
def student_database():
    if operating_system == 'Linux':
        os.system('clear')
    elif operating_system == 'Windows':
        os.system('cls')
    design.art('Student Database')

    try:
        with open('student_database.csv', 'r') as fr:
            data_table = from_csv(fr, field_names=['Student ID', 'Student Name', 'Age', 'Gender', 'Department','Course'])

        # Show student database
        print(data_table)
    except Exception as e:
        print(e)
        print('\nNot data available. Please add some student first.\n')

    choice = input('\nPlease enter your choice:\n'
                   '[1] Main Menu\n'
                   '\n'
                   'admin@sms:~$ ')

    if choice == '1':
        main.StartMain.main(self='self')
    else:
        print()
        print('[X] Wrong Input!')
        time.sleep(.50)
        if operating_system == 'Linux':
            os.system('clear')
        elif operating_system == 'Windows':
            os.system('cls')
        student_database()


def search_student(search='id'):
    if search == 'id':
        print('[1] Searching by ID')
    elif search == 'first_name':
        print('[2] Searching by First Name')


def search():
    if operating_system == 'Linux':
        os.system('clear')
    elif operating_system == 'Windows':
        os.system('cls')

    choice = input('Please enter your choice:\n'
                   '[1] Search by ID\n'
                   '[2] Search by First Name\n'
                   '[3] Back to Main Menu\n'
                   '\n'
                   'admin@sms:~$ ')
    if choice is '1':
        search_student(search='id')
    elif choice is '2':
        search_student(search='first_name')
    elif choice is '3':
        pass
    else:
        print()
        print('[X] Wrong Input!')
        time.sleep(.50)
        search()
