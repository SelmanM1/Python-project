import csv
import main
import time 
import os
import preloader
import header_design as design
class Student_Details:
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
    @staticmethod
    def student_info(operating_system):
        if operating_system == 'Linux':
            os.system('clear')
        elif operating_system == 'Windows':
            os.system('cls')
        tab='\t'
        design.art('New Student Form')
        student_id = Student_Details.id_generator()
        first_name = input('[+] Enter first name: ')
        middle_name = input('[+] Enter middle name: ')
        last_name = input('[+] Enter last name: ')
        age = input('[+] Enter age: ')
        gender = input('[+] Enter gender: ')
        department = input('[+] Enter department: ')
        course= input('[+] Enter course: ')

        while True:
            confirm = input('\n[!] Do you want to save? (y/n): ').lower()
            if confirm == 'y':
                if middle_name:
                    name = first_name + ' ' + middle_name + ' ' + last_name

                    # Saving information
                    with open('student_database.csv', 'a') as fs:
                        data = csv.writer(fs)
                        data.writerow([student_id, name, age, gender, department,course])
                else:
                    name = first_name + ' ' + last_name

                    # Saving information
                    with open('student_database.csv', 'a') as fs:
                        data = csv.writer(fs)
                        data.writerow([student_id, name, age, gender, department,course])
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

