
# import sqlite module
import sqlite3

# peopleValues is a tuple of tuples
peopleValues = (('Ron', 'Obvious', 42), ('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))

# establishes connection to database
with sqlite3.connect('test_database.db') as connection:
    # cursor that operates on the database
    c = connection.cursor()
    # deletes the table people if it already exists in the database
    c.execute("DROP TABLE IF EXISTS People")
    # creates table People
    c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
    # inserts the tuples from peopleValues into the People table
    c.executemany("INSERT INTO People VALUES(?,?,?)",
                  peopleValues)

    # sql query to get all the names where people's age is above 30
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    # fetchall() grabs all the results from the query
    for row in c.fetchall():
        print(row)

    # sql query to find the first and last name of people above the age of 30
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    # while the above query is true perform the following....
    while True:
        # fetchone() grabs one result from the query
        row = c.fetchone()
        # None keyword defines a null value or no value at all
        # if row has the value of None then (is true) then
        if row is None:
            # break keyword "jumps out" of a loop
            break
        #prints the row
        print(row)
        
