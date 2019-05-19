import cv2
from Jewel1AI import Jewel1AI

ai = Jewel1AI()
ai.launchGame()
image = ai.getWindowShot()
cv2.imshow("Image", image)
cv2.waitKey(0)