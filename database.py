import mysql.connector
import secrets

mydb = mysql.connector.connect(
    host = secrets.host,
    user = secrets.user,
    password = secrets.password,
    database = secrets.database 
)

barcode = '03STUNM137689541'

mycursor = mydb.cursor(dictionary=True)

mycursor.execute("SELECT barcode FROM parcels WHERE barcode LIKE '%s'AND delivery_status = 'undelivered';" % (barcode))

myresult = mycursor.fetchall()

amount = len(myresult)

if amount >= 1:
    print("sesam open u")

else:
    print("access denied")

#print(aantal)

#print(myresult)