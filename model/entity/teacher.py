from model.entity.person import Person
from tools.validator import Validator


# skill
class Teacher(Person):
    def __init__(self, id, name, family, salary, study,skill):
        self.id = id
        self.name = name
        self.family = family
        self.salary = salary
        self.study = study

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = Validator.salary_validator(salary, "invalid salary ")

    @property
    def study(self):
        return self._study

    @study.setter
    def study(self, name):
        self._name = Validator.name_validator(name, "invalid name ")

    @property
    def skill(self):
        return self._skill

    @skill.setter
    def skill(self, name):
        self._name = Validator.name_validator(name, "invalid name ")