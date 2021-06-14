from datetime import *

from datetime import datetime

import os

import shutil

# path to the folder where all the files are located
source = "C:\\Users\\Ricar\\Documents\\GitHub\\Python_Projects\\Transfer_assignment\\Files"

# path to where I want the files to go
destination = "C:\\Users\\Ricar\\Documents\\GitHub\\Python_Projects\\Transfer_assignment\\Destination"

# os.listdir() makes a list of all the files inside the directory in this case
# the path variable
fileNames = os.listdir(source)

# create a list consisting of absolute file paths
# range(len()) allows to iterate through the list fileName
for files in range((len(fileNames))):
    # define a list variable
    fileList = []
    # index of 0
    files = 0
    # while files is less than the length of the list fileName
    while files < len(fileNames):
        # creates an absolute path using os.path.join()
        # fileNames[files] is the element at index files
        abPath = os.path.join(source,fileNames[files])
        # adds it a the list lst
        fileList.append(abPath)
        files += 1

#create a list consisting of the last modified date from the list lst
for dates in range(len(fileList)):
    dates = 0
    dateList = []
    while dates < len(fileList):
        # os.path.getmtime() gets the time in seconds
        fileDate = os.path.getmtime(fileList[dates])
        # time.time() converts time into seconds
        timeOfFile = datetime.fromtimestamp(fileDate)
        dateList.append(timeOfFile)
        dates += 1

#creates a dictionary comprised of two lists
fileTime = dict(zip(fileList, dateList)
for value in fileTime.fromkeys(key, value):
    if value > (datetime.now() + timedelta(days=-1)):
        shutil.copyfiles(key, destination)
