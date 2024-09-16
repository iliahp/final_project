from model.entity.person import Person

# skill
class Teacher(Person):
    def __init__(self, id, name, family, salary, study):
        self.id = id
        self.name = name
        self.family = family
        self.salary = salary
        self.study = study

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    @property
    def study(self):
        return self._study

    @study.setter
    def study(self, value):
        self._study = value

