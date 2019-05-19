import cv2
from Jewel1AI import Jewel1AI
import pytesseract
import time

def showImage(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)

ai = Jewel1AI()
ai.launchGame()
ai.handleTitleScreen()