#Database connection
import mysql.connector
import secrets

#Relay & RGB LED
from gpiozero import OutputDevice, RGBLED

#Barcode reader
import de2120_barcode_scanner

#Other
import time