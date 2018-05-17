
# part 1
arr = [4, 6, 1, 3, 5, 7, 25]
def star(arr):
    for val in arr:
        print'*'*val

star(arr)


arr =[4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

for val in arr:
    if type(val) == str:
        print (val[0]*len(val)).lower()
    else:
        print"*"*val

