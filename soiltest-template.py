import time
import datetime
from datetime import date
import calendar
import RPi.GPIO as GPIO
from board import SCL, SDA
import busio
import math
from ISStreamer.Streamer import Streamer
from adafruit_seesaw.seesaw import Seesaw

# --------- User Settings ---------
SENSOR_LOCATION_NAME = "Plant"
BUCKET_NAME = "Soil Sensor"
BUCKET_KEY = "Bucket key here - keep speech marks"
ACCESS_KEY = "Access key here - keep speech marks"
MINUTES_BETWEEN_READS = 5
# ---------------------------------

i2c_bus = busio.I2C(SCL, SDA)
streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)
ss = Seesaw(i2c_bus, addr=0x36)
channel = 21
i = datetime.datetime.now()
curr_date = date.today()
hour = i.hour

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)
def pump_on(channel):
    GPIO.output(channel, GPIO.LOW)  # Turn pump on
def pump_off(channel):
    GPIO.output(channel, GPIO.HIGH)  # Turn pump off

while True:
    # read moisture level through capacitive touch pad
    touch = ss.moisture_read()

    # read temperature from the temperature sensor
    temp = ss.get_temp()
    tempr = math.trunc(temp)
    print((calendar.day_name[curr_date.weekday()]) + " " + (time.strftime("%H:%M")))
    print("Soil temperature: " + str(tempr) + ' degrees celcius' + "  Soil moisture: " + str(touch))

    if touch <= 500 and 7 < hour < 18:
        print('Watering is needed.')
        try:
            pump_on(channel)
            time.sleep(5)
            pump_off(channel)
            print("Watering completed. Next check in 15 minutes.")
            
            streamer.log(SENSOR_LOCATION_NAME + " Message", "Plants last watered at " + "\n" + (time.strftime("%H:%M")) + " on " + (calendar.day_name[curr_date.weekday()]))
            streamer.flush() #send data to Initial State dashboard
            time.sleep(900)  
            
        except KeyboardInterrupt:
            GPIO.cleanup()
    else:
        print('Watering is not needed. Next check in 15 minutes.')
        pump_off(channel)
        time.sleep(900) 
