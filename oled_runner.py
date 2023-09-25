from machine import Pin,I2C
import ssd1306
i2c = I2C(1,sda=Pin(18), scl=Pin(19), freq=400000)
lcd = ssd1306.SSD1306_I2C(128,64,i2c) #create LCD object,Specify col and row

