import csv
import main
import time 
import os
import preloader
import header_design as design
import sys
class Person:
    def __init__(self, firstname,middlename,lastname,age, gender):
        self.first_name = firstname
        self.middle_name=middlename
        self.last_name=lastname
        self.age=age
        self.gender=gender
    

class Student(Person):
    def __init__(self, firstname, middlename, lastname, age, gender, department, course):
        Person.__init__(self,firstname, middlename,lastname, age, gender)
        self.department = department
        self.course = course
        self.student_id = Student.id_generator()

    @staticmethod
    def get_user_input(operating_system):
        if operating_system == 'Linux':
            os.system('clear')
        elif operating_system == 'Windows':
            os.system('cls')
        design.art('New Student Form')
        info={}
        info['student_id']=Student.id_generator()
        info['first_name'] = input('[+] Enter first name: ')
        info['middle_name'] = input('[+] Enter middle name: ')
        info['last_name'] = input('[+] Enter last name: ')
        try:
            info['age']= int(input('[+] Enter age: '))
        except ValueError:
            print("Oops! That was no valid number. Try again...")
            sys.exit()
        info['gender'] = input('[+] Enter gender: ')
        info['department'] = input('[+] Enter department: ')
        info['course']= input('[+] Enter courses(comma seperated list): ').split(",")
        info['course']=" ".join(info['course'])
        return info
    @staticmethod
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

    def save_student_info(self,operating_system):
        tab='\t'
        while True:
            confirm = input('\n[!] Do you want to save? (y/n): ').lower()
            if confirm == 'y':
                if self.middle_name:
                    self.name = self.first_name + ' ' + self.middle_name + ' ' + self.last_name

                    # Saving information
                    with open('student_database.csv', 'a',newline='') as fs:
                        data = csv.writer(fs)
                        data.writerow([self.student_id, self.name, self.age, self.gender, self.department,self.course])
                else:
                    self.name = self.first_name + ' ' + self.last_name

                    # Saving information
                    with open('student_database.csv', 'a',newline='') as fs:
                        data = csv.writer(fs)
                        data.writerow([self.student_id, self.name, self.age, self.gender, self.department,self.course])
                print()

                msg = '[!] Please wait. \n\n' + tab * 4 + 'Saving'
                for i in range(5):
                    preloader.load(msg)
                print('\n[✔] Saved')
                time.sleep(.5)

                main.StartMain.main(self='self')
                break
            elif confirm == 'n':
                print()
                msg = tab * 4 + '[!] Please wait'
                for i in range(5):
                    preloader.load(msg)
                time.sleep(.5)
                main.StartMain.main(self='self')
                break
            else:
                print()
                print('[X] Wrong Input!')
                time.sleep(.50)

