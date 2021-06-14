from datetime import *

from datetime import datetime

import os

import shutil

# path to the folder where all the files are located
source = "C:\\Users\\Ricar\\Desktop\\Transfer_assignment\\Files"

# path to where I want the files to go
destination = "C:\\Users\\Ricar\\Desktop\\Transfer_assignment\\Destination"

# os.listdir() makes a list of all the files inside the directory in this case
fileNames = os.listdir(source)
print(fileNames)

for file in fileNames:
    # path for the file
    abPath = os.path.join(source, file)
    # gets time in a float
    modifySec = os.path.getmtime(abPath)
    # converts float in to datetime structure
    modifyTime = datetime.fromtimestamp(modifySec)
    
    # if the modyfied date is within the last day then copy over the file
    if modifyTime < (datetime.now() + timedelta(days=-1)):
        shutil.copyfile(abPath, destination)

    
    """if datetime.fromtimestamp(file) > (datetime.now() + timedelta(days=-1)):
        shutil.copyfiles(source, destination)"""