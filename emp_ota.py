from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://raw.githubusercontent.com/marcovanurk/MicroPython_OTA/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "emp_ota.py")
ota_updater.download_and_install_update_if_available()


print ('Hello World v1')
