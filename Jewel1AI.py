# This class holds information about our bot playing Bejeweled 1 game.
# Please note that this code will only support the Windows platform.
import cv2
import pyautogui
import os
import urllib.request as urllib
import win32gui
import time
import numpy as np
import pytesseract

class Jewel1AI:
    # Holds the class information about the AI
    def __init__(self):
        self.hwnd = 0
        #self.net = cv2.dnn.r cv2.dnn.readNet("frozen_east_text_detection.pb")

    def getWindowDimensions(self):
        rect = win32gui.GetWindowRect(self.hwnd)
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y
        return (x, y, w, h)

    def getWindowShot(self):
        region = self.getWindowDimensions()
        img = pyautogui.screenshot(region=region)
        return np.array(img)
        # Convert RGB to BGR 
        #open_cv_image = open_cv_image[:, :, ::-1].copy()

    def getPlayingFieldCoord(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (3, 3), 3)
        canny = cv2.Canny(gray, 50, 100)
        _, cnts, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contour = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
        return cv2.boundingRect(contour)

    def handleTitleScreen(self):
        canPlayNow = False
        gray = None
        W = 0
        H = 0
        x = 0
        y = 0
        while not canPlayNow:
            img = self.getWindowShot()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            endX = int(gray.shape[1] * (67/100))
            startX = int(gray.shape[1] * (1/4))
            startY = int(gray.shape[0] * (3/4))
            endY = int(gray.shape[0] * (7/8))
            gray = gray[startY:endY, startX:endX]
            text = pytesseract.image_to_string(gray)
            for line in text.split("\n"):
                if line == "CLICK HERE TO PLAY!":
                    canPlayNow = True
                    x = startX
                    y = startY
                    W = gray.shape[1]
                    H = gray.shape[0]
                    boxes = pytesseract.image_to_boxes(gray)
                    break
        region = self.getWindowDimensions()
        x += region[0]
        y += region[1]
        pyautogui.moveTo(x + 108, y + 31)
        pyautogui.click()
        #print(x, y, W, H)
        #for box in boxes.split("\n"):
        #    vals = box.split()
        #    print(vals)
        #print(boxes)
        #print(type(boxes))

    def launchGame(self):
        # Launch Bejeweled 1 and get the window handle.
        steamPath = "C:\Program Files (x86)\Steam\steamapps\common\Bejeweled Deluxe"
        if os.path.isdir(steamPath):
            os.system('"C:\Program Files (x86)\Steam\Steam.exe" steam://rungameid/3350')
        else:
            raise "Steam or the game isn't installed."
        hwnd = 0
        oneTimeCheck = True
        while hwnd == 0:
            hwnd = win32gui.FindWindow(None, "Bejeweled Deluxe 1.87")
            if hwnd != 0 and oneTimeCheck:
                oneTimeCheck = False
                hwnd = 0
                time.sleep(0.5)
        time.sleep(0.5)
        self.hwnd = hwnd
