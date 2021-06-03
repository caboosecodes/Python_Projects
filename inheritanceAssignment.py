
#creates a class vehicle()
class vehicle():
    #attributes 
    manufactuerer = ''
    model = ''
    year = ''
    fuel = ''


#child class truck()
class truck(vehicle):
    towing_capacity = 'lbs'
    drive_train = ''
    
#child class electricVehicle()
class electricVehicle(vehicle):
    charge_time = 'minutes'
    drive_range = 'miles'
