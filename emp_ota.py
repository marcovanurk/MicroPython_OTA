import time
from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://raw.githubusercontent.com/marcovanurk/MicroPython_OTA/"



while True:
    print ('Hello World v3')
    time.sleep(2.5)
    
    # check new version available
    ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "emp_ota.py")
    ota_updater.download_and_install_update_if_available()
