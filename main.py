import time
from machine import Pin

from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD



#
#
#
def GetNewVersion():
    # check new version available
    ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
    ota_updater.download_and_install_update_if_available()


led = Pin("LED", Pin.OUT) # 25 is 'Pico' and "LED" is 'Pico W'
firmware_url = "https://raw.githubusercontent.com/marcovanurk/MicroPython_OTA/"



#
# loop
#
while True:
    for i in range(0, 10):
        led.toggle()
        time.sleep(.25)
        
    GetNewVersion()
    

