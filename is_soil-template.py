
import time
from ISStreamer.Streamer import Streamer
from board import SCL, SDA
import busio
from adafruit_seesaw.seesaw import Seesaw

# --------- User Settings ---------
SENSOR_LOCATION_NAME = "Plant"
BUCKET_NAME = "Soil Sensor"
BUCKET_KEY = "Bucket key here"
ACCESS_KEY = "Access key here"
MINUTES_BETWEEN_READS = 0.25
# ---------------------------------

i2c_bus = busio.I2C(SCL, SDA)

ss = Seesaw(i2c_bus, addr=0x36)

streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)

while True:
    # read moisture level through capacitive touch pad
    touch = ss.moisture_read()

    # read temperature from the temperature sensor
    temp = ss.get_temp()
    tempr = format(temp, ".0f")

    streamer.log(SENSOR_LOCATION_NAME + " Moisture", touch)
    streamer.log(SENSOR_LOCATION_NAME + " Temperature", tempr)
    streamer.flush()

    time.sleep(60*MINUTES_BETWEEN_READS)
