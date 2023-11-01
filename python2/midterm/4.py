class Person():
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.address
    
    def setAddress(self):
        return f'address: {self.address}'
    
    def toString(self):
        return f'Person: name: {self.name}, address: {self.address}'

class Student(Person):
    def __init__(self, program, year, fee):
        super().__init__(self, name, address, program, year, fee)
        self.program = program
        self.year = year
        self.fee = fee

    def getProgram(self):
        return self.program

    def setProgram(self):
        return f'program: {self.program}'

    def getYear(self):
        return self.year

    def setYear(self):
        return f'year: {self.year}'

    def getFee(self):
        return self.fee

    def setFee(self):
        return f'fee: {self.fee}'

    def toString(self, name, address):
        return f'Student: Person(name: {name}, address: {address}), program: {self.program}, year: {self.year}, fee: {self.fee}'

class Staff(Person):
    def __init__(self, school, pay):
        super().__init__(self, name, address)
        self.school = school
        self.pay = pay
        
    def getSchool(self):
        return self.school

    def setSchool(self):
        return f'school: {self.school}'

    def getPay(self):
        return self.pay

    def setPay(self):
        return f'pay: {self.pay}'

    def toString(self, name, address):
        return f'Staff: (Person: name: {name}, address: {address}), school: {self.program}, pay: {self.pay}, fee: {self.fee}'

person = Person('Aisha', 35)
student = Student('mcm', 2023, 2.4)
staff = Staff('sam', 1.2)
print(person.getName, person.getAddress, person.setAddress, person.toString)
print(student.getProgram, student.setProgram, student.getYear, student.setYear, student.getFee, student.setFee, student.toString)
print(staff.getSchool, staff.setSchool, staff.getPay, staff.setPay, staff.toString)


    



        
    
        
        







