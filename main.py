import time
time.sleep(2)

import machine
#pi pico w
led = machine.Pin("LED", machine.Pin.OUT)
time.sleep(2)
led.off()
time.sleep(2)
led.on()

import basic_temp
