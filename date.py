import datetime
import time
import RPi.GPIO as GPIO
from datetime import date
import calendar
from board import SCL, SDA
import busio
import math
from ISStreamer.Streamer import Streamer
from adafruit_seesaw.seesaw import Seesaw

# --------- User Settings ---------
SENSOR_LOCATION_NAME = "Plant"
BUCKET_NAME = "Soil Sensor"
BUCKET_KEY = "ACDC5DULREW3"
ACCESS_KEY = "ist_VtzxLdTMbq-IEBvxWPfkqepP5iAqWVL3"
MINUTES_BETWEEN_READS = 5
# ---------------------------------
i2c_bus = busio.I2C(SCL, SDA)
streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)
channel = 20
i = datetime.datetime.now()
hour = i.hour
# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)
GPIO.setwarnings(False)

def lights_on(channel):
    GPIO.output(channel, GPIO.LOW)  # Turn lights on

def lights_off(channel):
    GPIO.output(channel, GPIO.HIGH)  # Turn lights off

while True: 
    print (time.strftime("%H:%M"))
    if hour > 5 and hour < 19:
        try:
            print('lights on')
            lights_on(channel)
            streamer.log(SENSOR_LOCATION_NAME + "Lights status", "Lights are:" + "\n" + "ON")
            streamer.flush() #send data to Initial State dashboard
        
        except KeyboardInterrupt:
            lights_off(channel)
            GPIO.cleanup()
        
    else:
        print('lights off')
        lights_off(channel)
        streamer.log(SENSOR_LOCATION_NAME + "Lights status", "Lights are:" + "\n" + "OFF")
        streamer.flush() #send data to Initial State dashboard
    time.sleep(300)
