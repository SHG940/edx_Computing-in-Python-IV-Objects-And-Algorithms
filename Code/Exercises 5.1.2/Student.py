import Person


class Student:
    def __init__(self, student: Person = None, gpa=0.0, credit_hours=0, enrolled=True, classes=[]):
        self.person = student
        self.gpa = gpa
        self.credit_hours = credit_hours
        self.enrolled = enrolled
        self.classes = classes

    def __str__(self):
        return f"Student's Name: {self.person.first_name} {self.person.last_name}\n" \
               f'GPA: {self.gpa}\n' \
               f'CreditHours: {self.credit_hours}\n' \
               f'Enrolled: {self.enrolled}\n' \
               f'Amount of Classes: {len(self.classes)}'
