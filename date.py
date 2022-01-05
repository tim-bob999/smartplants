import datetime
import time
import RPi.GPIO as GPIO

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
    try:
        if hour > 5 and hour < 19:
            print('lights on')
            lights_on(channel)
        else:
            print('lights off')
            lights_off(channel)
    except:
        print('time check failed')
    time.sleep(900)
