# Harry and jude.
# This is the code we had setup to eventually run with the potato in the cannon

import math
import time
import Adafruit_LSM303
import datetime


RST = 24
lsm303 = Adafruit_LSM303.LSM303() # creates LSM303 initialization


while True:
	accel, mag = lsm303.read() 
	accel_x, accel_y, accel_z = accel # initializes the acceleration for x y and z
	mag_x, mag_y, mag_z = mag 

   	print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(accel_x, accel_y, accel_z, mag_x, mag_y, mag_z)) # Prints out the values we want, x y and z acceleration
	time.sleep(.5) # waits half a second 
