#!/usr/bin/python3

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import urllib.request
import time
import paho.mqtt.client as mqtt

# MQTT
# Add here ip, port, cid, username and password from broker
broker = '<ip>'
port = 1883
clientid = 'doorpen'
username = '<usrname>'
password = '<pwd>'

# Add here ip from cam
url = '<ip>'


prev = ""
pres = ""
while True:
    img_resp = urllib.request.urlopen(url+'cam-hi.jpg')
    imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    frame = cv2.imdecode(imgnp, -1)
    #_, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        pres = obj.data
        if prev == pres:
            pass
        else:
            print("Data: ", obj.data)
            # MQTT Connection
            client1 = mqtt.Client(clientid)
            client1.username_pw_set(username, password)
            client1.connect(broker, port)
            client1.loop_start()
            client1.publish("house/qrcode", obj.data)
            client1.disconnect()
            client1.loop_stop()
