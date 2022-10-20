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
            print(barcode)
            scan_buffer = ""

            mydb = mysql.connector.connect(
                host = secrets.host,
                user = secrets.user,
                password = secrets.password,
                database = secrets.database 
            )

            mycursor = mydb.cursor()

            mycursor.execute("SELECT * FROM parcels WHERE 1")

            myresult = mycursor.fetchall()

            print(myresult)
            control_lock()


        time.sleep(0.02)


def control_lock():

    relay = OutputDevice(16)

    led = RGBLED(26, 19, 13)

    
    relay.on()
    led.color = (0,1,1)
    time.sleep(5)
    relay.off()
    led.color = (1,1,0)


if __name__ == '__main__':
    main()