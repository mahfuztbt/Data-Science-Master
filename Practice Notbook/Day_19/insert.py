import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("insert into test1.test_table values(3433, 'rony', 343, 'mahfuz')")
mydb.commit()
mydb.close()