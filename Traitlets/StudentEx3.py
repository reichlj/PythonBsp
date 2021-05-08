import traitlets

class Student(traitlets.HasTraits):
    studentId = traitlets.Int()
    studentName = traitlets.Unicode()

    def __init__(self, studentId):
        self.studentId = studentId

    @traitlets.default("studentName")
    def _get_default_name(self):
        return "Pappu"

student6 = Student(2)

print("Student ID : ", student6.studentId)
print("Student Name : ", student6.studentName)