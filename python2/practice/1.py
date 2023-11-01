"""import math
class Point:
    def __init__(self, xCoord=0, yCoord=0):
        self.__xCoord = xCoord
        self.__yCoord = yCoord
       
    # get x coordinate
    def get_xCoord(self):
        return self.__xCoord
   
    # get y coordinate
    def get_yCoord(self):
        return self.__yCoord
   
    # set x coordinate
    def set_xCoord(self, xCoord):
        self.__xCoord = xCoord
       
    # set y coordinate
    def set_yCoord(self, yCoord):
        self.__yCoord = yCoord
       
    # get current position
    def get_position(self):
        return self.__xCoord, self.__yCoord
   
    # change x & y coordinates by p & q
    def move(self, p, q):
        self.__xCoord += p
        self.__yCoord += q
       
    # overload + operator
    def __add__(self, point_ov):
        return Point(self.__xCoord + point_ov.__xCoord, self.__yCoord + point_ov.__yCoord)
    
    def __sub__(self, point_ov):
        return Point(self.__xCoord - point_ov.__xCoord, self.__yCoord - point_ov.__yCoord)

    def __mul__(self, point_ov):
        return Point(self.__xCoord * point_ov.__xCoord, self.__yCoord * point_ov.__yCoord)
        
    def __truediv__(self, point_ov):
        return Point(self.__xCoord / point_ov.__xCoord, self.__yCoord / point_ov.__yCoord)
   
    # overload > (greater than) operator
    def __gt__(self, point_ov):
        return math.sqrt(self.__xCoord**2 + self.__yCoord**2) > math.sqrt(point_ov.__xCoord**2 + point_ov.__yCoord**2)

point = Point(3, 3)

class Circle(Point):
    def __init__(self, point, radius=1):
        self.point=point
        self.__radius = radius
    
    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        self.__radius = radius
    
    def area(self):
        return math.pi * (self.__radius**2)
    
    def length(self):
        return 2 * math.pi * self.__radius
    
    def intersects(self, other_circle):
        distance_between_centers = math.sqrt((self.get_xCoord() - other_circle.get_xCoord())**2 + (self.get_yCoord() - other_circle.get_yCoord())**2)
        return distance_between_centers < self.__radius + other_circle.get_radius()

circle = Circle(point,5)

print("area:", circle.area())
print("length:", circle.length())
"""

import math

class Point:
    def __init__(self, xCoord=0, yCoord=0):
        self.__xCoord = xCoord
        self.__yCoord = yCoord
    
    def get_xCoord(self):
        return self.__xCoord
    
    def get_yCoord(self):
        return self.__yCoord
    
    def set_xCoord(self, xCoord):
        self.__xCoord = xCoord
    
    def set_yCoord(self, yCoord):
        self.__yCoord = yCoord
    
    def get_position(self):
        return self.__xCoord, self.__yCoord
    
    def move(self, p, q):
        self.__xCoord += p
        self.__yCoord += q
    
    def __add__(self, point_ov):
        return Point(self.__xCoord + point_ov.__xCoord, self.__yCoord + point_ov.__yCoord)
    
    def __sub__(self, point_ov):
        return Point(self.__xCoord - point_ov.__xCoord, self.__yCoord - point_ov.__yCoord)
    
    def __mul__(self, point_ov):
        return Point(self.__xCoord * point_ov.__xCoord, self.__yCoord * point_ov.__yCoord)
    
    def __truediv__(self, point_ov):
        return Point(self.__xCoord / point_ov.__xCoord, self.__yCoord / point_ov.__yCoord)
    
    def __gt__(self, point_ov):
        return math.sqrt(self.__xCoord**2 + self.__yCoord**2) > math.sqrt(point_ov.__xCoord**2 + point_ov.__yCoord**2)

class Circle(Point):
    def __init__(self, point, radius=1):
        super().__init__(point.get_xCoord(), point.get_yCoord())
        self.__radius = radius
    
    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        self.__radius = radius
    
    def area(self):
        return math.pi * (self.__radius**2)
    
    def length(self):
        return 2 * math.pi * self.__radius
    
    def intersects(self, other_circle):
        distance = math.sqrt((self.point.__xCoord - other_circle.get_xCoord())**2 + (self.get_yCoord() - other_circle.get_yCoord())**2)
        return distance < self.__radius + other_circle.get_radius()

point1 = Point(3, 3)
circle1 = Circle(point1, 5)

point2 = Point(8, 8)
circle2 = Circle(point2, 3)

print("area1:", circle1.area())
print("length1:", circle1.length())
print("area2:", circle2.area())
print("length2:", circle2.length())

if circle1.intersects(circle2):
    print("\ncircle 1 intersects circle 2")
else:
    print("circle 1 does not intersect circle 2")


"""
point1 = Point(1, 2)
point2 = Point(3, 4)

add = point1 + point2
sub = point2 - point1
mul = point2 * point1
div = point2 / point1
print("Sum:", add.get_position())
print("Sub:", sub.get_position())
print("Mul: ", mul.get_position())
print("Div:", div.get_position())
"""
