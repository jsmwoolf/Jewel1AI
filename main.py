import cv2
from Jewel1AI import Jewel1AI
import pytesseract
import time

def showImage(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)

ai = Jewel1AI()
ai.launchGame()
image = ai.getWindowShot()
showImage("Image", image)

time.sleep(1)
image = ai.getWindowShot()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
endX = int(gray.shape[1] * (2/3))
startY = int(gray.shape[0] * (3/4))
gray = gray[startY:, :endX]
showImage("Grayscale", gray)
text = pytesseract.image_to_string(gray)
for line in text.split("\n"):
    print("Line: {}".format(line))