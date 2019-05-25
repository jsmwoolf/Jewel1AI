import cv2
from Jewel1AI import Jewel1AI
import pytesseract
import time
import numpy as np

def showImage(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)

#ai = Jewel1AI()
#ai.launchGame()
#ai.handleTitleScreen()
#time.sleep(2)
#img = ai.getWindowShot()
#cv2.imwrite("test.png", img)
img = cv2.imread("test.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 3)
canny = cv2.Canny(gray, 50, 100)
_, cnts, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
print("Min X value {}".format(cv2.boundingRect(contour)))