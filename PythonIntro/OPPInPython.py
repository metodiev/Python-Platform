class Parent:  # define parent class
    def myMethod(self):
        print
        'Calling parent method'


class Child(Parent):  # define child class
    def myMethod(self):
        print
        'Calling child method'


c = Child()  # instance of child
c.myMethod()  # child calls overridden method


class Animal:
    # initilize constructor and attributes
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self):
        return self.name + "is eating"

    def sleep(self):
        return self.name + "is going to sleep!"

    def wakeUp(self):
        return self.name + "is waking up!"


class Gorilla(Animal):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def climbTrees(self):
        return self.name + " is climbing trees!"

    def poundChest(self):
        return self.name + "is pounding its chest!"


gorila = Gorilla("Kiro gorilata", 151)
animal = Animal("Animal", 123)
print(gorila.eat())
print(animal.eat())
print(gorila.climbTrees())