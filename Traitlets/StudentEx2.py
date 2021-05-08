import traitlets

class Student(traitlets.HasTraits):
    studentId = traitlets.Int()
    studentName = traitlets.Unicode()

    def __init__(self):
        pass

student5 = Student()

print("Student ID : ", student5.studentId)
print("Student Name : ", student5.studentName)