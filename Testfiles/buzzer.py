from gpiozero import Buzzer
import time

bz = Buzzer(17)
while True:
    bz.on()
    time.sleep(10)
    bz.off()
    time.sleep(5)