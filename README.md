# pico_thermostat
Simple Thermostat using a Raspberry Pi Pico

This Circuit will use a 2222 npn transistor to control a 12V DC fan if the dht20 detects the temperature is over a threshold you define, using the pico.

**Credits**
|[dht20 driver](https://github.com/flrrth/pico-dht20)|[ssd1306  driver](https://github.com/stlehmann/micropython-ssd1306/blob/master/ssd1306.py)|[Circuit and Image](https://forums.raspberrypi.com/viewtopic.php?t=219897&sid=7d5c8cef37829fa4a5cbb0610ec2d0c3)|

This is the basic premise using the transitor:
![Basic Circuit using a transistor](tc.jpg)

Pico Pi Pin Setup to Transistor:

Collector - Black Wire of the DC fan
Base      - 470 Ohm resistor to power/+ on  breadboard rail
Emitter   - Black wire of the 12 V power
	        and to ground/- on the breadboard rail
Pico GPIO 15   - to power/+ on the  breadboard rail
Pico Pin 38 (gnd) to ground/- on the breadboard rail (shared ground)
Red wire of the 12 V power supply - to red  wire of the DC Fan 

Pics:
TBD

Other Connections:
TBD

Install:
TBD

