from gpiozero import GPIODevice

doorsensor = GPIODevice(pin=21)

if doorsensor.is_active:
    print("toe")

else:
    print("open")