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
    read_barcode()

def read_barcode():
    my_scanner = de2120_barcode_scanner.DE2120BarcodeScanner()


    scan_buffer = ""
    barcode = ""

    while True:
        scan_buffer = my_scanner.read_barcode()
        if scan_buffer:
            barcode = str(scan_buffer)
            scan_buffer = ""

            print(barcode)

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

            else:
                pass


        time.sleep(0.02)


def control_lock():

    relay = OutputDevice(16)

    led = RGBLED(26, 19, 13)

    
    relay.on()

    led.color = (0,1,1)
    time.sleep(5)
    relay.off()

if __name__ == '__main__':
    main()