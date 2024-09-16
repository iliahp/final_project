from model.entity.course import Course
from tools.validator import Validator


class Selectcourse:
    def __init__(self, id, course, teacher, student, date_time, score):
        self.id = id
        self.course = course
        self.teacher = teacher
        self.student = student
        self.date_time = date_time
        self.score = score

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def course(self):
        return self.course

    @Course.setter
    def course(self, value):
        self._course = value

    @property
    def teacher(self):
        return self.teacher.setter

    def teacher(self, name):
        self._name = Validator.name_validator(name, "invalid name ")

    @property
    def score(self):
        return self.score.setter

    def score(self, score):
        self._score = Validator.score_validator(score, "invalid score ")

    @property
    def date_time(self):
        return self.date_time.setter

    def date_time(self, value):
        self._date_time = value
