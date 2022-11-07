from datetime import datetime


class Person:
    def __init__(self, first_name='[no first name]', last_name='[no last name]',
                 eye_color='[no eye color]', birthdate: datetime = None):
        self.first_name = first_name
        self.last_name = last_name
        self.eye_color = eye_color
        self.birthdate = birthdate

    def get_age(self):
        if self.birthdate is not None:
            now = datetime.now()
            years = now.year - self.birthdate.year

            if now.month < self.birthdate.month or (now.month == self.birthdate.month and now.day < self.birthdate.day):
                years -= 1

            return years

        return None
