import mysql.connector
import secrets

mydb = mysql.connector.connect(
    host = secrets.host,
    user = secrets.user,
    password = secrets.password,
    database = secrets.database 
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM parcels")

myresult = mycursor.fetchall()

print(myresult)