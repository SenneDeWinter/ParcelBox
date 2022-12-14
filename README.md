# ParcelBox
A DIY parcel locker using Raspberry Pi. The locker is connected to a MySQL database to check if scanned parcels are registered in the database. 
## Components
- Raspberry Pi 4 2GB
- SparkFun 2D Barcode Scanner Breakout
- DFRobot Gravity: Digital 5A Relay Module
- Lock-style Solenoid - 12VDC
- Generic Green LED
- Generic Buzzer
- Generic Step Down Regulator
## Software
- Python script that checks if the scanned barcode is known in the database, then opens the lock and updates the delivery status
- MySQL Database
- PHPMyAdmin
- PHP page to insert new parcels into the database
- PHP page to check the delivery status of parcels
- PM2 to start python script on boot
## Other Hardware
- Custom 3D printed RPi case
- Custom lasercut box to house the pi and other components
- 12V 2A Power Supply

## Schematic
![Schematic](/Images/ParcelBox_bb.png)