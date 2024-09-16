import re
from datetime import datetime, date


class Validator:
    @classmethod
    def name_validator(cls, name, message):
        if isinstance(name, str) and re.match(r"^[a-zA-Z\s]{2,30}$", name):
            return name
        else:
            raise ValueError(message)

    @classmethod
    def username_validator(cls, username, message):
        if re.match(r"^[\w@!#$%^&*\s]{2,30}$", username):
            return username
        else:
            raise ValueError(message)

    @classmethod
    def password_validator(cls, password, message):
        if re.match(r"^[\w@!#$%^&*\s]{2,16}$", password):
            return password
        else:
            raise ValueError(message)

    @classmethod
    def national_id_validator(cls, national_id, message):
        if isinstance(national_id, str) and re.match(r"^[0-9]{10}$", national_id):
            return national_id
        else:
            raise ValueError(message)
#birthdate
#todo

    @classmethod
    def phone_number_validator(cls, phone_number, message):
        if isinstance(phone_number, str) and re.match(r"^[0-9]{11}$", phone_number):
            return phone_number
        else:
            raise ValueError(message)

    @classmethod
    def salary_validator(cls, salary, message):
        if isinstance(salary, str) and re.match(r"^[0-9]{2-14}$", salary):
            return salary
        else:
            raise ValueError(message)

    @classmethod
    def score_validator(cls, score, message):
        if isinstance(score, str) and re.match(r"^[0-20]{2}$", score):
            return score
        else:
            raise ValueError(message)

