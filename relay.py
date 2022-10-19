from ast import While
from gpiozero import OutputDevice
import time

relay = OutputDevice(16)

while True:
    relay.on()
    time.sleep(5)
    relay.off() 