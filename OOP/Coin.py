
import random

number_flip= 5000
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
        print 'Attempt #', attemp,'Throwing a coin... Its a Tail! ... Got',count_head, 'head(s) so far and', count_tail, 'tail(s) so far'
print "Ending the program, thank you!"
