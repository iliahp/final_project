from model.entity.person import Person

# grade
class Validator:
    pass


class Student(Person):
    def __init__(self, id, name, family, national_id,grade):
        self.id = id
        self._name = name
        self.family = family
        self.national_id = national_id

    @property
    def national_id(self):
        return self._national_id

    @national_id.setter
    def national_id(self, national_id):
        self.national_id = Validator.national_id_validator(national_id, "invalid number ")



    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value




