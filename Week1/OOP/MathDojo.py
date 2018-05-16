class MathDojo(object):
    def __init__(self, start):
        self.arg1 = start

    def add(self, *x):
        for a in x:
            if type(a) == list or type(a) == tuple:
                for value in a:
                    self.arg1 += value 
            else:
                self.arg1 = self.arg1 + a 
        return self
    
    def subtract(self, *x):
        for a in x:
            if type(a) == list or type(a) == tuple:
                for value in a:
                    self.arg1 -= value 
            else:
                self.arg1 = self.arg1 - a 
        return self
    def result(self):
        print self.arg1

md = MathDojo(0)
#smd.add(2).add(2,5).subtract(3,2).result
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()


# class Calculator(object):
#     def __init__(self,*vals):
#         self.vals = vals #list of vals here

#     def add(self):
#         return sum(self.vals)
#     class Calculator(object):
