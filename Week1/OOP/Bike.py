

# class Bike(object):
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.logged = True
#     def login(self):
#         self.logged = True
#         print self.name + " is logged in."
#         return self
#     def logout(self):
#         self.logged = False
#         print self.name + " is not logged in"
#         return self
#     def show(self):
#         print "My name is {}. You can email me at {}".format(self.name, self.email)
#         return self

class Human(object):
    def __init__(self, name, height, weight):
        print "creating a human"
        self.name = name
        self.height = height
        self.weight = weight
        self.health = 100

Awsome = Human ("Jon", 1, 3)

print Awsome.name 

def verbalattack( self, target):
    print "arrg"
    target.health 

class Warrior(Human):
    def __init__(self, name, height, weight, strength):
        super(Warrior, self).__init__(name, height, weight)
        print "creating a Warrior"
        self.stregth = strength
        self.health *= 2

    def verbalattack

Warrior1 = Warrior('stef curry', 1000, 1, 100) 
print Warrior1

