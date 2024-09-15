import re
class employee:
    def __init__(self, id, name, family, salary):
        self.id = id
        self.name = name
        self.family = family
        self.salary = salary

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if re.match(r"^[a-zA-Z\s]{2,20}$", value):
            self._name = value
        else:
            self._name = None

    def __str__(self):
        return f"{self.__dict__}"
