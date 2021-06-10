

import shutil
import os

# set where the source of the files are
source = "C:\\Users\\Ricar\\Desktop\\FolderA\\"

# set the destination path to folderB
destination = "C:\\Users\\Ricar\\Desktop\\FolderB\\"
files = os.listdir(source)

for i in files:
    # we are saying move the files represented by 'i' to their new destination
    shutil.move(source + i, destination)

