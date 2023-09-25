import gc
import time
from machine import Pin, I2C
from utime import sleep

OLED=True
if OLED:
    from oled_runner import lcd

TEMP=True
if TEMP:
    #VCC, SDA, GND, SCL
    i2c0_sda = Pin(12)
    i2c0_scl = Pin(13)
    i2c0 = I2C(0, sda=i2c0_sda, scl=i2c0_scl)
    from dht20 import DHT20
    dht20 = DHT20(0x38, i2c0)

transitor=True
if transitor:
    transitor = Pin(15, Pin.OUT)
    transitor_sleep=5

ADA=False
if ADA:
    import urequests as requests
    aio_key = "key"
    username = "user"
    feed_name = "temperature"
    url = 'https://io.adafruit.com/api/v2/' + username + '/feeds/' + feed_name + '/data'
    headers = {'X-AIO-Key': aio_key, 'Content-Type': 'application/json'}

count=0
measurements=0
TRIGGER_TEMP=75

def thermo_stat():
    if fahrenheit > TRIGGER_TEMP:
        #If on, turn off (transitor.value(0) sets GPIO high)
        if transitor.value() == 0:
            print("Turning on the fan via the transistor")
            transitor.value(1)
        else:
            print("transitor value already", transitor.value())
    else:
        print("Turning off the fan via the transistor")
        transitor.value(0)
        
def oled_show():
    lcd.fill(0)
    lcd.show()
    lcd.text(f"Temp: {fahrenheit} F",0,0)
    lcd.show()
    
def thermometer():
    global fahrenheit
    measurements = dht20.measurements
    celcius = measurements['t']
    fahrenheit = (celcius * 1.8) + 32
    fahrenheit = round(fahrenheit, 2)
    print(f"Temp: {fahrenheit} °F, humidity: {measurements['rh']} %RH")

def ada():
    #Ada
    body = {'value': str(fahrenheit)}
    print('sending to ad/io')
    r = requests.post(url, json=body, headers=headers)
    print(r.text)
  
  
while True:
    thermometer()
    oled_show()
    print("Wait...")
    time.sleep(1)
    #ada()
    gc.collect()
    thermo_stat()
    sleep(15)
    
    
