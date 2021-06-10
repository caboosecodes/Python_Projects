

from datetime import *


def branchOpen():

    utcNow = datetime.now(timezone.utc)
    londonTime = utcNow + timedelta(hours = 1)
    nycTime = utcNow + timedelta(hours = -4)
    portlandTime = utcNow + timedelta(hours = -7)
    #print(utcNow)
    #print(londonTime)
    #print(nycTime)
    #print(portlandTime)

    london9am = londonTime.replace(hour = 9, minute = 0, second = 0, microsecond = 0)
    london5pm = londonTime.replace(hour = 17, minute = 0, second = 0, microsecond = 0)
    
    if londonTime > london5pm or londonTime < london9am:
        print("London branch is closed")
    elif londonTime >= london9am:
        print("London branch is open")
    
    nyc9am = nycTime.replace(hour = 9, minute = 0, second = 0, microsecond = 0)
    nyc5pm = nycTime.replace(hour = 17, minute = 0, second = 0, microsecond = 0)        
    
    if nycTime > nyc5pm or nycTime < nyc9am:
        print("New York branch is closed")
    elif nycTime >= nyc9am:
        print("New York branch is open")
    

    portland9am = portlandTime.replace(hour = 9, minute = 0, second = 0, microsecond = 0)
    portland5pm = portlandTime.replace(hour = 17, minute = 0, second = 0, microsecond = 0)        
    
    if portlandTime > portland5pm or portlandTime < nyc9am:
        print("Portland branch is closed")
    elif portlandTime >= portland9am:
        print("Portland branch is open")


if __name__ == "__main__":
    branchOpen()
