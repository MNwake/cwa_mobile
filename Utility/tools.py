from datetime import datetime


def calculate_age(date_of_birth):
    date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%dT%H:%M:%S')

    today = datetime.today()
    age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    return age