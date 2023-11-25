from mfrc522 import MFRC522
import utime

import network
import socket
from time import sleep

import machine
import requests

import secrets

ssid = 'DEMONET'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
print("starting connect")
wlan.connect(ssid, secrets.wifi_password)
while wlan.isconnected() == False:
        print('Waiting for connection...')
        utime.sleep_ms(1000)
print("connect done")

reader = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0)

detected = None

while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            if detected != card:
                #requests.get(f"http://{secrets.backend_ip}")
                print(f"Card changed!: old={detected} new={card}")
                detected = card
            continue
    if detected is not None:
        print(f"Card changed!: old={detected} new={None}")
        detected = None

