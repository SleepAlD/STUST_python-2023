class Student :

    def __init__(self) -> None:
        pass

    def getSchoolName(self):
        print(f"School Name : {self.school}")

    def setSchoolName(self, school):
        self.school = school

    def getStudentName(self):
        print(f"Student Name : {self.name}")

    def setStudentName(self, name):
        self.name = name

    def getSchoolAdress(self):
        print(f"School Adress : {self.school_adress}")

    def setSchoolAdress(self, school_adress):
        self.school_adress = school_adress

    def getdepartment(self):
        print(f"Student Department : {self.department}")

    def setdepartment(self, department):
        self.department = department

    def getsid(self):
        print(f"Student ID : {self.sid}")

    def setsid(self, sid):
        self.sid = sid

    def getadress(self):
        print(f"Student Adress : {self.adress}")

    def setadress(self, adress):
        self.adress = adress

    def getdcn(self):
        print(f"Teacher Name : {self.dcn}")

    def setdcn(self, dcn):
        self.dcn = dcn

    def getscore(self):
        print(f"Student Score : {self.score}")

    def setscore(self, score):
        self.score = score

    def getGPA(self):
        print(f"Student's GPA' : {self.GPA}")

    def setGPA(self, GPA):
        self.GPA = GPA

Johny = Student()

Johny.setSchoolName('STUST')
Johny.setSchoolAdress('Taiwan')
Johny.setStudentName('Johny')
Johny.setdepartment('Computer')
Johny.setsid('4G0F1125')
Johny.setdcn('Gay')
Johny.setscore(50)
Johny.setGPA(3.3)
Johny.setadress('Kaushoung')

print("\n*---------------------------------------*")
Johny.getSchoolName()
Johny.getSchoolAdress()
Johny.getStudentName()
Johny.getdepartment()
Johny.getsid()
Johny.getdcn()
Johny.getscore()
Johny.getGPA()
Johny.getadress()
print("*---------------------------------------*\n")