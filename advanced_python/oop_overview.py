class Student():

    #class object attribute
    planet = "Earth"

    #class instance attributes
    def __init__(self, name: str, gpa: float) -> None:
        self.name = name
        self.gpa = gpa


class Agent():

    origin = "USA"

    def __init__(self, name: str, height: int, weight: int) -> None:
        self.name = name
        self.height = height
        self.weight = weight


class Circle():

    pi = 3.14

    def __init__(self, radius: float ) -> None:
        self.radius = radius

    def area(self) -> int:
        return (self.radius**2) * Circle.pi
    
    def perimeter(self) -> int:
        return (2 * self.radius) * Circle.pi


mycircle = Circle(4.7)

print(mycircle.area())

print(mycircle.perimeter())


x = Agent("Travis", "6", "180")


travis = Student("travis", 4.0)
mimi = Student("mimi", 3.5)

print(x.name)
x.name = "Busen"
print(x.name)
