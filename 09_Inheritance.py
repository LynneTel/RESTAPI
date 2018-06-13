class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(marks) / len(marks)

    def friend(self, friend_name):
        return Student(friend_name, self.school)


# anna = Student("Anna", "Oxford")
# friend = anna.friend("Greg")
# print(friend.name)
# print(friend.school)


###

# class WorkingStudent(Student):
#     def __init__(self, name, school, salary):
#         super().__init__(name, school)
#         self.salary = salary
#
#
# rolf = WorkingStudent("Rolf", "Harvard", 20.00)
# sue = rolf.friend("Sue")
# print(sue.salary)  # Error!
#

###

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(marks) / len(marks)

    @classmethod
    def friend(cls, origin, friend_name, *args, **kwargs):
        return cls(friend_name, origin.school, *args, **kwargs)


class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title


anna = WorkingStudent("Anna", "Oxford", 20.00, "Software Developer")
print(anna.salary)
friend = WorkingStudent.friend(anna, "Greg", 17.5, job_title="Software Developer")
print(friend.name)
print(friend.school)
print(friend.salary)


# rolf = WorkingStudent("Rolf", "Harvard", 20.00)
# sue = WorkingStudent.friend(rolf, "Sue", 15.00)
# print(sue.salary)  # This works!
