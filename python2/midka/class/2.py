class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def __str__(self):
        return  f'{self.name}, {self.age}, {self.grade}'
p1 = Student('John', 20, 100)
print(p1)
