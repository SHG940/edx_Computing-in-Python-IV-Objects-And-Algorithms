from Student import Student
from Person import Person

if __name__ == '__main__':
    person_instance = Person(first_name='Some', last_name='Guy')
    student_instance = Student(student=person_instance, credit_hours=15)
    print(str(student_instance))

    print('************************')
    # Changing values
    student_instance.person.first_name = 'Another'
    student_instance.gpa = 3.9
    student_instance.credit_hours = 1334
    student_instance.classes = ["CS1301", "PHYS3001", "ISYE3029"]
    print(str(student_instance))

    # Using dictionaries
    dic_student = {'first_name': 'Some', 'last_name': 'Guy'}
    print(dic_student)
