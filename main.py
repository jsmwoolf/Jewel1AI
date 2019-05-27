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
cv2.imwrite("testImage.png", cv2.cvtColor(ai.getWindowShot(), cv2.COLOR_BGR2RGB))
print(ai.getPlayingFieldInfo(), file=open("SampleBoard.txt", "w"))