#Class created for vehicle
class vehicle:
    #creating function and activating init method
    def __init__ (self, max_speed, mileage): #----Self used----#
        self.max_speed = max_speed
        self.mileage = mileage
model = vehicle(240, 18) #----Creating object of class vehicle----#
print("The maximum speed is:", model.max_speed)
print("The mileage is:", model.mileage)         #----Printing the values of attributes----#