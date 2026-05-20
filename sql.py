import sqlite3

# Coonecting to sqlite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert record, create table and retrieve 
cursor = connection.cursor()

# Creating the table
# table_info = """
# Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);

# """

# cursor.execute(table_info)

# Inserting some records
# cursor.execute("INSERT INTO STUDENT VALUES('Sudhanshu', 'Data Science', 'B', 100)")
# cursor.execute("INSERT INTO STUDENT VALUES('Darius', 'Data Science', 'A', 86)")
# cursor.execute("INSERT INTO STUDENT VALUES('Virat', 'Data Science', 'A', 90)")
# cursor.execute("INSERT INTO STUDENT VALUES('Vikash', 'Devops', 'A', 50)")
# cursor.execute("INSERT INTO STUDENT VALUES('Vikram', 'Devops', 'A', 35)")

# Displaying all the records
print("The inserted records are: ")

data = cursor.execute("SELECT * FROM STUDENT ORDER BY NAME ASC")
for row in data:
    print(row)

# Closing the connection
connection.commit()
connection.close()