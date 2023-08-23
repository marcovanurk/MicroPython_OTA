import time
import machine
from machine import Pin, I2C

from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

import ssd1306



#
#
#
def GetNewVersion():
    # check new version available
    ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
    ota_updater.download_and_install_update_if_available()



led = Pin("LED", Pin.OUT) # 25 is 'Pico' and "LED" is 'Pico W'
firmware_url = "https://raw.githubusercontent.com/marcovanurk/MicroPython_OTA/"


# using default address 0x3C
i2c = I2C(0, sda=Pin(12), scl=Pin(13))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

#
# loop
#
while True:
    displayText = "version 1.0"
    display.text(displayText, 0, 0, 1)
    display.show()
    
    for i in range(30, 0, -1):
        display.text(str(i), 63, 32, 1)
        display.show()
        time.sleep(1.0)
        display.text(str(i), 63, 32, 0)
        
    #GetNewVersion()
    
    #machine.reset()

