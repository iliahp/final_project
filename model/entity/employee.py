from model.entity.person import Person


# salary
class Employee(Person):
    def __init__(self, id, name, family, salary):
        self.id = id
        self.name = name
        self.family = family
        self.salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value
