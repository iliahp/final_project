from model.entity.employee import Employee
from model.entity.student import Student
from model.entity.teacher import Teacher

#p1=Person(1,"ilia","hasanpour")
#print(p1.__dict__)
std1 = Student(1, "ali123", "alipour", "1234")
print(std1)
emp1 = Employee(4,"ilia","alipour",250)
print(emp1)

#emp1.name="ali4
tech1=Teacher(4,"reza","rezaii",5600,"python")
print(tech1)
