import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="Vindhesh",passwd="Qwerty@1",database="vindhesh")

mycursor = mydb.cursor()

name = "Chitra"
college_name = "I.Y"

# query = (f"insert into student values('{name}','{college_name}');")
# print(query)
# mycursor.execute(query)

mycursor.execute("select * from student;")
result = mycursor.fetchmany(100)
# status = print(mycursor._affected_rows())
for i in result:
    print(i)