# id, select_course, amount, description

class Payment:
    def __init__(self, id, select_course, amount, description):
        self.id = id
        self.select_course = select_course
        self.amount = amount
        self.description = description

    def __str__(self):
        return f"{self.__dict__}"

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def select_course(self):
        return self._select_course

    @select_course.setter
    def select_course(self, value):
        self._select_course = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value

    @property
    def desciription(self):
        return self._description

    @desciription.setter
    def desciription(self, value):
        self._description = value
