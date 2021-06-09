# Harry and jude.
# This is the code we had setup to eventually run with the potato in the cannon
import math
import time
import Adafruit_LSM303
import datetime


RST = 24
lsm303 = Adafruit_LSM303.LSM303() 


while True:
	accel, mag = lsm303.read() 
	accel_x, accel_y, accel_z = accel 
	mag_x, mag_y, mag_z = mag 

   	print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))
	time.sleep(.2)
