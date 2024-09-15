from school.models import person


#todo

class teacher(person):
    def __init__(self, id, name, family, salary, study):
        self.id = id
        self.name = name
        self.family = family
        self.salary = salary
        self.study = study

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

    @property
    def study(self):
        return self.__study

    @study.setter
    def study(self, value):
        self.__study = value

    def __str__(self):
        return f"{self.__dict__}"
