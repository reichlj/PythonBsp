import traitlets
class StudentSimple:
    def __init__(self, studentId, studentName):
        self.studentId = studentId
        self.studentName = studentName

class Student(traitlets.HasTraits):
    studentId = traitlets.Int()
    studentName = traitlets.Unicode()

    def __init__(self, studentId, studentName):
        self.studentId = studentId
        self.studentName = studentName

student3 = Student(2, "Putin")
print("Student ID : ", student3.studentId)
print("Student Name : ", student3.studentName)

try:
    student3.studentId = 1.5
except Exception as e:
    print(e)

try:
    student3.studentName = True
except Exception as e:
    print(e)
try:
    student4 = Student("Fake", False)
except Exception as e:
    print(e)