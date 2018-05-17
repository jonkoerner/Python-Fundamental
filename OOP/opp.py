'''
# declare a class and give it name User
class User(object):
    # the __init__ method is called every time a new object is created
    def __init__(self, name, email):
        # set some instance variables. just like any variable we can call these anything
        self.name = name
        self.email = email
        self.logged = False
    # this is a method we created to help a user login
    def login(self):
        self.logged = True
        print self.name + " is logged in."
        return self
#now create an instance of the class
new_user = User("Anna","anna@anna.com")
print new_user.email


class User(object):
    name = "Anna"
anna = User()
print "anna's name: ", anna.name
User.name = "Bob"
print "anna's name after change:", anna.name
bob = User()
print "bob's name:", bob.name

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False
user1 = User("Anna Propas", "anna@anna.com")
print user1.name
print user1.logged
print user1.email
'''
'''name = "Zen"
print "My name is", name
print "My name is " + name

first_name = "Zen"
last_name = "Coder"
print "My name is {} {}".format(first_name, last_name)
'''

'''
context = {
    'questions': [
        { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
        { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
        { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
        { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
    ]
 }

for key, data in context.items():
    #print data
    for value in data:
        print "Question #", value["id"], ": ", value["content"]
        print "----"
'''
import random

number_flip= 1000000
attemp = 0
count_head= 0 
count_tail= 0 
for flip in range(1,number_flip+1):
    attemp= attemp+1
    # random.random()
    if random.random()<.5:
        count_head = count_head + 1
        print 'Attempt #', attemp,'Throwing a coin... Its a head! ... Got',count_head, 'head(s) so far and', count_tail, 'tail(s) so far'
    else:
        count_tail = count_tail + 1
        print 'Attempt #', attemp,'Throwing a coin... Its a head! ... Got',count_head, 'head(s) so far and', count_tail, 'tail(s) so far'
print "Ending the program, thank you!"