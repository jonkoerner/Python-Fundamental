class Animal(object):
    def __init__(self, name, health):
        self.name = name 
        self.health = 100

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health = self.health - 5
        return self

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(self, name)
        self.health = 150
    
    def pet(self):
        self.health += 5
        return self

dog = Dog("chewy")
dog.pet().run().run().walk().walk().walk()
# print dog.health

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(self, name)
        self.health = 170

    def fly(self):
        self.health -= 10
    
    def displayhealth():
        print(self.health)

dragon = Dragon("puff")
print dragon.health