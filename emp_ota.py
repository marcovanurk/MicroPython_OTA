from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://raw.githubusercontent.com/marcovanurk/MicroPython_OTA/"

while True:
    print ('Hello World v2')
    time.sleep(2500)
    
    # check new version available
    ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "emp_ota.py")
    ota_updater.download_and_install_update_if_available()
