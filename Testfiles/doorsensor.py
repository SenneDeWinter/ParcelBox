from gpiozero import InputDevice, Buzzer
import time


doorsensor = InputDevice(4, pull_up=True)
bz = Buzzer(17)

while True:
    waarde = doorsensor.value
    if waarde == 0:
        bz.on()
    
    elif waarde == 1:
        bz.off()
