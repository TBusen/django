# base class (parent class)

class Person():

    def __init__(self, fname: str, lname: str) -> None:
        self.fname = fname
        self.lname = lname

    def hello(self) -> None:
        print("hello!")

    def report(self) -> None:
        print(f"I am {self.fname} {self.lname}")



class Agent(Person):

    def __init__(self, fname: str, lname: str, code_name) -> None:
        super().__init__(fname, lname)
        self.code_name = code_name

    def report(self) -> None:
        print("I am here")

    def reveal(self, passcode):

        if passcode == 123:
            print("I am a secret agent")
        else:
            self.report()



class Animal():
    
    def __init__(self, name: str, species: str) -> None:
        self.name = name
        self.species = species
        
        
    def greet(self) -> None:
        print(f"Hi! My name is {self.name} and I am a {self.species}")
        
        
class Dog(Animal):
    
    def sound(self) -> None:
        print("ruff")
        
class Cat(Animal):
    
    def sound(self) -> None:
        print("meow")
        
        



dogo = Dog("piper", "labrador")
dogo.sound()


x = Agent("John", "Smith", "mr.x")
x.reveal(325)
print(x.code_name)


#x = Person("John", "Smith")
#x.hello()
#x.report()



#derived class (child class)