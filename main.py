#Database connection
import mysql.connector
import secrets

#Relay & RGB LED
from gpiozero import OutputDevice, RGBLED

#Barcode reader
import de2120_barcode_scanner

#Other
import time

def main():
    while True:
        read_barcode()
        check_db()

def read_barcode():
    my_scanner = de2120_barcode_scanner.DE2120BarcodeScanner()


    scan_buffer = ""
    global barcode
    barcode = ""

    while True:
        scan_buffer = my_scanner.read_barcode()
        if scan_buffer:
            barcode = str(scan_buffer)
            scan_buffer = ""
            exit
            return barcode
            

        time.sleep(0.02)

def check_db():
    mydb = mysql.connector.connect(
        host = secrets.host,
        user = secrets.user,
        password = secrets.password,
        database = secrets.database 
    )

    mycursor = mydb.cursor(dictionary=True)

    mycursor.execute("SELECT barcode FROM parcels WHERE barcode = '%s' AND delivery_status = 'undelivered';" % (barcode))

    myresult = mycursor.fetchall()

    amount = len(myresult)

    if amount >= 1:
        control_lock()
        #add UPDATE query

    else:
        pass

def control_lock():

    relay = OutputDevice(16)

    led = RGBLED(26, 19, 13)

    
    relay.on()

    led.color = (0,1,1)
    time.sleep(5)
    relay.off()

if __name__ == '__main__':
    main()