class Animal(object):
    def __init__(self, name, food):
        self.name = name
        self.food = food
        print(f"Im eating {food}, {name}!")

class Dog(Animal):
    def __init__(self, name, thing):
        # Dog inherits from Animal
        Animal.__init__(self, name, "dog food") 
        # call parent
        print(f"he goes after the {thing}!")
        self.thing = thing

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self, "Cat", "milk")

d = Dog("Ranger", " ball")


a = Animal("Buddy", "bones")


print(d.name)
print(d.food)
print(d.thing)

