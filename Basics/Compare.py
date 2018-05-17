list_one = [1, 2, 5, 6, 2]
list_two = [1, 2, 5, 6, 2]
list_one1 = [1, 2, 5, 6, 5]
list_two1 = [1, 2, 5, 6, 5, 3]
list_one2 = [1, 2, 5, 6, 5, 16]
list_two2 = [1, 2, 5, 6, 5]
list_one3 = ['celery', 'carrots', 'bread', 'milk']
list_two3 = ['celery', 'carrots', 'bread', 'cream']
# def Compare_Lists(arr, arr2):
arr = [1,2,5,6,2]
arr2 = [1,2,5,6,2]
def Compare_Lists(arr, arr2):
    if arr == arr2:
        print "The lists are the same." 
    else:
        print "The lists are not the same."
 
Compare_Lists(list_one, list_two)
Compare_Lists(list_one1, list_two1)
Compare_Lists(list_one2, list_two2)



