# importing mysql.connector module.
import mysql.connector

# creating a connection to the database.
conx = mysql.connector.connect(host="localhost",user="Vindhesh",passwd="Qwerty@1",database="vindhesh")

# Setting a cursor usinng cursor() method that would store our sql queries. 
mycursor = conx.cursor()



try:
    #input the user data and store in respective variable.
    name = input("Enter your name: ")
    college_name = input("Enter your college name:")

    #creating a query for my-sql.
    query = (f"insert into students values('{name}','{college_name}');")

    # inserting query in cursor.
    mycursor.execute(query)

finally:
    #commiting the changes to database.  
    conx.commit()

    #getting the information of rows affected
    print(mycursor.rowcount, "Record Inserted")

    #getting the data updated data in the table
    mycursor.execute("select * from students;")

    #creating a loop to fetch data stored in cursor as a response
    result = mycursor.fetchmany(100)
    for i in result:
        print(i)

