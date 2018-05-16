'''users = {
    'Students': [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}

for x in users:
    print x
    # print users[x]
    for y in users[x]:
        print y
        for z in y:
            print y[z]
    # for i in list:'''
       
    # len(student['first_name'])+len(student['last_name'])
    # for value in data:
    #     print value['first_name']
'''
users = {
    'Students': [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}

for x in users:
    print x
    count= 1
    # print users[x]
    for y in users[x]:
        print count,"-", y['first_name'],y['last_name'],"-", len(y['first_name']+y['last_name'])
        count += 1
        # for z in y:
        #     print y[z]
'''

# # function input
# my_dict = {
#   "Speros": "(555) 555-5555",
#   "Michael": "(999) 999-9999",
#   "Jay": "(777) 777-7777"
# }
# new= ()
# for i in my_dict:
#     new = new + (i , my_dict[i]) 
# print new
        



#function output
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]


list1 = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
list2 = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
    new_dict = {}
    new_dict = zip(list1,list2)
    print new_dict


make_dict(list1,list2)


