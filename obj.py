

class Person:

    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
    
    def printName(self):
        print(f"name:{self.name}")



class SuperHuman(Person):

    power = "fly"

    def __init__(self, name,age,country):
        self.name = name
        self.age = age
        self.country = country


person = Person("Ansh", 18, "India")


person.printName()


superhuman = SuperHuman("Ram", 21, "USA") 

print("superhumanpower:{}", format(superhuman.__class__.power))

print(f"superhumanname:{superhuman.printName()}")


## inheritance

class Bird:
    def __init__(self, name="Default", colour="white", canFly=False):
        self.name = name
        self.colour = colour
        self.canFly = canFly
    

    def whoisthis(self):
        print(f"BirdName:{self.name}")
    
    def colour(self):
        print(f"colour:{self.colour}")

    
class Penguin(Bird):

    # inherit from parent class bird constructor
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    
    def whoisthis(self):
        print("This is penguin")

    def printcolour(self):
        print(f"colour:{self.colour}")


bird = Bird()

pengu = Penguin()

pengu.whoisthis()

# inherited method from parent 
pengu.printcolour()


# encapsulation 

class Employee:
    def __init__(self, age, salary):
        self.age = age
        # private variable start with __
        self.__salary = salary

    def printAge(self, age):
        print(f"age is:{age}")


emp = Employee("Raj", 1000)

print(emp)

emp.printAge(22)


class Computer:
    
    def __init__(self, price=1000):
        self.__price = price

    def setPrice(self, price):
        self.__price = price

    def __str__(self):
        return f"price:{self.__price}"


cmp1 = Computer()

print(cmp1)

cmp1.setPrice(900)

print(cmp1)

del cmp1

print(cmp1)
