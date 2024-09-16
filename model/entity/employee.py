from model.entity.person import Person
import re
from tools.validator import Validator


# salary
class Employee(Person):
    def __init__(self, id, name, family, salary):
        self.id = id
        self.name = name
        self.family = family
        self.salary = salary

    @property
    def name(self):
           return self._name

    @name.setter
    def name(self, name):
        self._name = Validator.name_validator(name , "invalid name ")
