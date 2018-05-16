# for i in range(,2001,2):
#     print 'Number is', i,'. This is and an odd Number.'
#     print 'Number is', (i+1),'. This is and an even Number.'


# def multiply(arr,b):

#     for val in arr:
#         print val * b

# arr= [2,4,10,16]
# b=5

# multiply(arr,b)


# def layered_multiples(arr):
  # your code here
# b=3
# arr = [2,4,5]
# for val in arr:
#         print ['1,'*val*b]


# import random
# print random. random()

# from random import*
# randint(60, 100)

# import random
# random_num = random.random(60, 100)

import random

def grade(reps):
    print "Scores and Grades"
    for x in range(0, reps):
        score = random.randint(60, 101)
        if score >= 60 and score <= 69:
            print "Score: ", score,"; Your grade is D"
        elif score >= 70 and score <= 79:
            print "Score: ", score, "; Your grade is C"
        elif score >= 80 and score <= 89:
            print "Score: ", score, "; Your grade is B"
        elif score >= 90 and score <= 100:
            print "Score: ", score, "; Your grade is A"
        else:
            print "You failed"
    print "End of the program.  Bye!"

grade(10)

print grade