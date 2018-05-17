class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayInfo(self):
        print self.price
        print self.max_speed
        print self.miles
    
    def ride(self):
        print 'Riding' 
        self.miles +=10
        return self

    
    def reverse(self):
        print 'Reversing'
        if self.miles >0:
            self.miles -=6
        return self
        


bike1 = Bike(200,30) 

# instance1
bike1.ride().ride().ride()
bike1.reverse()
bike1.displayInfo()

# # instancec2
# bike1.ride()
# bike1.ride()
# bike1.reverse()
# bike1.reverse()
# bike1.displayInfo()

# # instance3
# bike1.reverse()
# bike1.reverse()
# bike1.reverse()






        



# def displayinfo():
#     print self.price





