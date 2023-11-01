class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.address
    
    def setAddress(self, address):
        self.address = address
        return f'Address updated to: {self.address}'
    
    def toString(self):
        return f'Person: name: {self.name}, address: {self.address}'

class Student(Person):
    def __init__(self, name, address, program, year, fee):
        super().__init__(name, address)
        self.program = program
        self.year = year
        self.fee = fee

    def getProgram(self):
        return self.program

    def setProgram(self, program):
        self.program = program
        return f'Program updated to: {self.program}'

    def getYear(self):
        return self.year

    def setYear(self, year):
        self.year = year
        return f'Year updated to: {self.year}'

    def getFee(self):
        return self.fee

    def setFee(self, fee):
        self.fee = fee
        return f'Fee updated to: {self.fee}'

    def toString(self):
        return f'Student: {super().toString()}, program: {self.program}, year: {self.year}, fee: {self.fee}'

class Staff(Person):
    def __init__(self, name, address, school, pay):
        super().__init__(name, address)
        self.school = school
        self.pay = pay
        
    def getSchool(self):
        return self.school

    def setSchool(self, school):
        self.school = school
        return f'School updated to: {self.school}'

    def getPay(self):
        return self.pay

    def setPay(self, pay):
        self.pay = pay
        return f'Pay updated to: {self.pay}'

    def toString(self):
        return f'Staff: {super().toString()}, school: {self.school}, pay: {self.pay}'

# Creating instances
person = Person('Aisha', 'Address 1')
student = Student('John', 'Address 2', 'Engineering', 2023, 2500)
staff = Staff('Sarah', 'Address 3', 'XYZ School', 3000)

# Testing the methods
print(person.getName())
print(person.getAddress())
print(person.setAddress('New Address'))
print(person.toString())

print(student.getProgram())
print(student.setProgram('Computer Science'))
print(student.getYear())
print(student.setYear(2024))
print(student.getFee())
print(student.setFee(2700))
print(student.toString())

print(staff.getSchool())
print(staff.setSchool('ABC School'))
print(staff.getPay())
print(staff.setPay(3500))
print(staff.toString())
