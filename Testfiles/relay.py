from gpiozero import OutputDevice, LED
import time

relay = OutputDevice(16)

led = LED(26)

while True:
    relay.on()
    led.on()
    time.sleep(5)
    relay.off()
    led.off()
    time.sleep(5) 