import re


class Student:
    def __init__(self, id, name, family, national_id):
        self.id = id
        self._name = name
        self.family = family
        self.national_id = national_id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if re.match(r"^[a-zA-Z\s]{2,20}$", value):
            self._name = value
        else:
            self._name = None

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, value):
        if re.match(r"^[a-zA-Z\s]{2,20}$", value):
            self._family = value
        else:
            self._family = None

    @property
    def national_id(self):
        return self._national_id

    @national_id.setter
    def national_id(self, value):
        self._national_id = value

    def __str__(self):
        return f"{self.__dict__}"
