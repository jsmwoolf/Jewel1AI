import cv2
from Jewel1AI import Jewel1AI
import pytesseract
import time
import numpy as np

def showImage(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)

ai = Jewel1AI()
ai.launchGame()
ai.handleTitleScreen()
time.sleep(2)
print(ai.getPlayingFieldInfo())
#cv2.imwrite("test.png", img)
#img = cv2.imread("test.png")
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#gray = cv2.GaussianBlur(gray, (3, 3), 3)
#canny = cv2.Canny(gray, 50, 100)
#_, cnts, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#contour = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
#print(contour)
#(x, y, w, h) = cv2.boundingRect(contour)
#print((x, y, w, h))
#croppedImg = img[y:y+h, x:x+w]
#showImage("Cropped Image", croppedImg)
#showImage("Cropped Image", croppedImg[12:64, 12:64])
"""
redFilter = cv2.inRange(croppedImg, np.array([0, 0, 128]), np.array([0, 0, 255]))
showImage("Red Image", redFilter)

whiteFilter = cv2.inRange(croppedImg, np.array([200, 200, 200]), np.array([255, 255, 255]))
showImage("White Image", whiteFilter)

yellowFilter = cv2.inRange(croppedImg, np.array([0, 128, 128]), np.array([0, 255, 255]))
showImage("Yellow Image", yellowFilter)

blueFilter = cv2.inRange(croppedImg, np.array([128, 128, 0]), np.array([255, 255, 0]))
showImage("Blue Image", blueFilter)

purpleFilter = cv2.inRange(croppedImg, np.array([128, 0, 128]), np.array([255, 0, 255]))
showImage("Purple Image", purpleFilter)

orangeFilter = cv2.inRange(croppedImg, np.array([0, 64, 170]), np.array([0, 128, 255]))
showImage("Orange Image", orangeFilter)

greenFilter = cv2.inRange(croppedImg, np.array([32, 150, 32]), np.array([150, 255, 150]))
showImage("Green Image", greenFilter)
"""