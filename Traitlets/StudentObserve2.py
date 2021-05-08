import traitlets

class Student(traitlets.HasTraits):
    studentId = traitlets.Int()
    studentName = traitlets.Unicode()
    studentAddress = traitlets.Dict()

    def __init__(self, studentId, studentName):
        self.studentId = studentId
        self.studentName = studentName

    @traitlets.observe("studentAddress")
    # @traitlets.observe("studentAddress", "studentName")
    def monitor_address_change(self, addr_change_details):
        print("Old Address : ", addr_change_details["old"])
        print("New Address : ", addr_change_details["new"])

student8 = Student(7, "Boris")
print("Student ID : ", student8.studentId)
print("Student Name : ", student8.studentName)
print("Student Address : ", student8.studentAddress)
student8.studentAddress = {"Country" : "India", "State": "Gujarat", "City": "Surat"}
