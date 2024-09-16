import re

from tools.validator import Validator


# id, name, family, birth_date, national_id, phone_number
class Person:
    def __init__(self, id, name, family, birthday, phone_number):
        self.id = id
        self.name = name
        self.family = family

    def __str__(self):
        return f"{self.__dict__}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = Validator.name_validator(name, "invalid name ")

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = Validator.family_validator(family, "invalid family ")

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        self._birthday = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = Validator.phone_number_validator(phone_number, "invalid phone_number ")
