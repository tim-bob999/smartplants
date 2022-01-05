# smartplants

Automated pot plant watering system

I started here: https://medium.com/.../how-to-use-a-soil-moisture-sensor...
This covers the sensors and online dashboard. I didn't use a light sensor. You can get a i2c hub and could then connect more sensors for additional plants.

I then bought a 5V relay which was known to work at 3.3v from the GPIO pins:
https://core-electronics.com.au/5v-4-channel-relay-module...
and grow lights and peristaltic pump:
https://www.ebay.com.au/sch/i.html?_from=R40...
This worked well to water slowly and at low pressure. 

https://www.ebay.com.au/itm/294283531275?hash=item4484aa540b:g:65oAAOSwoNVg9T~B
The pump and lights are connected to a 12v power supply through the relays.

You can view the dashboard here: https://go.init.st/n5c3k17

Scripts:
date checks the current hour and turns the lights on if it is daytime and off if not.
soiltest checks the time and soil moisture level, watering if dry but only during the daytime
issoil streams soil moisture and temperature to the Initial State dashboard.

I would appreciate any feedback on simplifying my scripts and fixing my noob errors (but it works so I can't have done it too badly!).
