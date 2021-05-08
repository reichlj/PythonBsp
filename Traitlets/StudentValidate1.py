import traitlets

class Student(traitlets.HasTraits):
    studentId = traitlets.Int()
    studentName = traitlets.Unicode()
    studentAddress = traitlets.Dict()

    def __init__(self, studentId, studentName):
        self.studentId = studentId
        self.studentName = studentName

    @traitlets.validate("studentId")
    def _validate_id(self, student_id_details):
        #student_id_details.keys() dict_keys(['trait', 'value', 'owner'])
        if student_id_details["value"] <1 or student_id_details["value"] >50:
            raise traitlets.TraitError("Student ID should be between 1-50. Invalid Value : %d"%(student_id_details["value"]))
        return student_id_details["value"]

    @traitlets.validate("studentAddress")
    def _validate_address(self, student_addr_details):
        if "Country" not in student_addr_details["value"]:
            raise traitlets.TraitError("Country is compulsary in Address. Invalid Value : %s"%(str(student_addr_details["value"])))
        return student_addr_details["value"]


student10 = Student(1, "Elon")
student10.studentId = 10
try:
    student10.studentId = -1
except Exception as e:
    print(e)

student11 = Student(10, "Bill")
student11.studentAddress = {"Country":"US", "State":"NY", "City":"NY"}
try:
    with student11.hold_trait_notifications():
            student11.studentAddress = {"Country":"US","State":"NY", "City":"NY"}
            student11.studentId = -2
except Exception as e:
    print(e)