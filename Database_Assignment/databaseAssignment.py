

# imports the os module
import os


# imports the sqlite3 module
import sqlite3

#connects and creates database
conn = sqlite3.connect('test.db')

#while this connection is open do the following
with conn:
    # cur will be operating on the database
    cur = conn.cursor()
    # creates a table if its not present
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        fileName TEXT)')

    #saves the changes 
    conn.commit()

# path to where the files are held
# needs "\\" to avoid a unicode error
path = "C:\\Users\\Ricar\\Documents\\GitHub\\Python_Projects\\Database_Assignment"


# os.listdir() creates a list of the files stored at a path
fileNames = os.listdir(path)

# turns the list into a tuple
tupleNames = tuple(fileNames)

# for every file in the list fineName
for file in tupleNames:
    # if a file that ends with ".txt is true, do the following
    if file.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            # insert that file into tbl_files
            # YOU NEED [] brackets around file
            cur.execute('INSERT INTO tbl_files (fileName) VALUES (?)', \
                        [file])
            # prints file
            print('Files with the .txt extension: {}\n'.format(file))

# closes the connection
conn.close
