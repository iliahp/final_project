from model.entity.person import Person

# grade
class Student(Person):
    def __init__(self, id, name, family, national_id):
        self.id = id
        self._name = name
        self.family = family
        self.national_id = national_id

    @property
    def national_id(self):
        return self._national_id

    @national_id.setter
    def national_id(self, value):
        self._national_id = value





