l = ["hello",19,98.98,10,"World",11]
# for i in range(0,len(l)-1):
#print (type(l[i]))
string=""
sum =0
for i in range(0,len(l)):
    if type(l[i]) != type(l[len(l)-1]):
        print "The list you entered is of mixed type"
        break
    elif type(l[i]) == type(l[len(l)-1]):
        if i != len(l):
            continue
        print( "The list you entered is", type(l[0]))
for i in range(0,len(l)-1):
    if type(l[i]) == str:
        string = string + l[i]
    else:
        sum = sum + l[i]
print ('String: '+string)
print 'sum', sum   
