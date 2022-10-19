from gpiozero import OutputDevice, RGBLED
import time

relay = OutputDevice(16)

led = RGBLED(26, 19, 13)

while True:
    relay.on()
    led.color = (0,1,1)
    time.sleep(5)
    relay.off()
    led.color = (1,1,0)
    time.sleep(5) 