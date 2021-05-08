import traitlets

class Student(traitlets.HasTraits):
    studentId = traitlets.Int()
    studentName = traitlets.Unicode()
    studentAddress = traitlets.Dict()

    def __init__(self, studentId, studentName):
        self.studentId = studentId
        self.studentName = studentName

def monitor_address_change(addr_change_details):
    # type(addr_change_details):  <class 'traitlets.utils.bunch.Bunch'>
    # addr_change_details.keys(): dict_keys(['name', 'old', 'new', 'owner', 'type'])
    print(addr_change_details)
    print("Old Address : ", addr_change_details["old"])
    print("New Address : ", addr_change_details["new"])

student7 = Student(7, "Angela")
student7.observe(monitor_address_change, names = ["studentAddress"])

print("Student ID : ", student7.studentId)
print("Student Name : ", student7.studentName)
print("Student Address : ", student7.studentAddress)

student7.studentAddress = {"Country" : "India", "State": "Gujarat", "City": "Surat"}
