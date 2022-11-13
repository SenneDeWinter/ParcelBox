#Database connection
import mysql.connector
import secrets

#GPIOZero
from gpiozero import OutputDevice, LED, InputDevice, Buzzer

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
            return      

        time.sleep(0.02)

def check_db():
    mydb = mysql.connector.connect(
        host = secrets.host,
        user = secrets.user,
        password = secrets.password,
        database = secrets.database 
    )

    if barcode == secrets.barcode:
        control_lock()
    
    else:
        mycursor = mydb.cursor(dictionary=True)
        mycursor2 = mydb.cursor()

        mycursor.execute("SELECT barcode FROM parcels WHERE barcode = '%s' AND delivered = 0;" % (barcode))

        myresult = mycursor.fetchall()

        amount = len(myresult)

        if amount >= 1:
            control_lock()
            mycursor2.execute("UPDATE parcels SET delivered = 1 WHERE barcode = '%s';" % (barcode))
            mydb.commit()

        else:
            pass

def control_lock():

    relay = OutputDevice(16)

    led = LED(26)

    
    relay.on()

    led.on()

    time.sleep(5)

    relay.off()

    time.sleep(3)

    check_door()

def check_door():
    doorsensor = InputDevice(4, pullup=True)
    bz = Buzzer(17)

    while True:
        waarde = doorsensor.value
        if waarde == 0:
            bz.on()
    
        elif waarde == 1:
            bz.off()
            break

if __name__ == '__main__':
    main()