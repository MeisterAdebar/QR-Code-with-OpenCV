import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import urllib.request

#cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

# Add here ip from cam
url = '<ip>'
cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)

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
            print("Type:", obj.type)
            print("Data: ", obj.data)
            prev = pres
        cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                    (255, 0, 0), 3)

# cv2.imshow() method is used to display an image in a window. The window automatically fits to the image size.
# Syntax: cv2.imshow(window_name, image)
# Parameters:
# window_name: A string representing the name of the window in which image to be displayed.
# image: It is the image that is to be displayed.
# Return Value: It doesn’t returns anything.
    cv2.imshow("live transmission", frame)

 # waitkey() function of Python OpenCV allows users to display a window for given milliseconds or until any key is pressed.
 # It takes time in milliseconds as a parameter and waits for the given time to destroy the window,
 # if 0 is passed in the argument it waits till any key is pressed.
    key = cv2.waitKey(1)
    if key == 27:
        break

# destroyAllWindows() function allows users to destroy or close all windows at any time after exiting the script.
# If you have multiple windows open at the same time and you want to close then you would use this function.
# It doesn’t take any parameters and doesn’t return anything.
# It is similar to destroyWindow() function but this function only destroys a specific window unlike destroyAllWindows().
#
cv2.destroyAllWindows()
