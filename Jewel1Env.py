# This class holds information about the Bejeweled 1 game environment.
# Please note that this code will only support the Windows platform.
import cv2
import pyautogui
import os
import urllib.request as urllib
import win32gui
import time
import numpy as np
import pytesseract

class Jewel1Env:
    # Holds the class information about the AI
    def __init__(self):
        self.hwnd = 0
        self.moves = 0
        self.dialog = False
        # This is only needed for the first move
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
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

    def _getPlayingFieldCoord(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (3, 3), 3)
        canny = cv2.Canny(gray, 50, 100)
        _, cnts, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contour = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
        return cv2.boundingRect(contour)

    def _moveDialog(self, img):
        cropped = img[10:200, 10:300] #cv2.cvtColor(img[10:200, 10:300], cv2.COLOR_BGR2RGB)
        filteredImg = cv2.inRange(cropped, np.array([56, 67, 154]), np.array([96, 134, 167]))
        uniques, counts = np.unique(filteredImg, return_counts=True)
        counts = dict(zip(uniques, counts))
        if 255 in counts:
            (winX, winY, winW, winH) = self.getWindowDimensions()
            (areaX, areaY, w, h) = self._getPlayingFieldCoord(self.getWindowShot())
            winX += areaX
            winY += areaY
            pyautogui.moveTo(winX + 300, winY + 90)
            pyautogui.drag(0, w, duration=.5)
            time.sleep(.25)

    def getPlayingField(self):
        img = self.getWindowShot()
        (x, y, w, h) = self._getPlayingFieldCoord(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img[y:y+h, x:x+w]

    def getPlayingFieldInfo(self):
        # Responsible for getting the information
        (x, y, _, _) = self.getWindowDimensions()
        pyautogui.moveTo(x,y)
        croppedImage = None
        if self.moves == 0:
            img = self.getWindowShot()
            if self.dialog == False:
                (self.x, self.y, self.w, self.h) = self._getPlayingFieldCoord(img)
                self._moveDialog(img[self.y:self.y+self.h, self.x:self.x+self.w])
                self.dialog = True
                img = self.getWindowShot()
            croppedImage = cv2.cvtColor(img[self.y:self.y+self.h, self.x:self.x+self.w],  cv2.COLOR_BGR2RGB)
        else:
            croppedImage = self.getPlayingField()
        # The ordering for the limits follows:
        # 1) Red
        # 2) White
        # 3) Yellow
        # 4) Blue
        # 5) Purple
        # 6) Orange
        # 7) Green 
        colors = [
            "R",
            "W",
            "Y",
            "B",
            "P",
            "O",
            "G"
        ]
        lowerLimits = [
            np.array([0, 0, 128]),
            np.array([145, 145, 145]), 
            np.array([0, 128, 128]),
            np.array([128, 128, 0]),
            np.array([128, 0, 128]),
            np.array([0, 64, 170]),
            np.array([32, 150, 32])
        ]
        higherLimits = [
            np.array([0, 0, 255]),
            np.array([175, 175, 175]), 
            np.array([0, 255, 255]),
            np.array([225, 225, 0]),
            np.array([255, 0, 255]),
            np.array([0, 128, 255]),
            np.array([150, 255, 150])
        ]
        matrix = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]
        ]
        spacing = 52
        for multipleY in range(1,9):
            for multipleX in range(1,9):
                imgSeg = croppedImage[8 + (spacing*(multipleY-1)):8 + (spacing*multipleY), 12 + (spacing*(multipleX-1)):12 + (spacing*(multipleX))]
                highestCount = 0
                theColor = "N/A"
                for (lower, higher, color) in zip(lowerLimits, higherLimits, colors):
                    filteredImg = cv2.inRange(imgSeg, lower, higher)
                    uniques, counts = np.unique(filteredImg, return_counts=True)
                    counts = dict(zip(uniques, counts))
                    if 255 in counts and counts[255] > highestCount:
                        if counts[255] < 50 and color == "W":
                            continue
                        highestCount = counts[255]
                        theColor = color
                matrix[multipleY-1][multipleX-1] = theColor
        return matrix

    def makeMove(self, x, y, direction):
        (winX, winY, winW, winH) = self.getWindowDimensions()
        img = None
        areaX = 0
        areaY = 0
        w = 0
        h = 0
        while areaX == 0 or areaY == 0:
            # Sometimes, a mis-fire occurs when trying to grab the field
            # coordinates.  As a result, we should take a shot as many
            # times as needed
            img = self.getWindowShot() 
            if self.moves == 0:
                # Only needed once.  Additional moves won't execute
                (areaX, areaY, w, h) = (self.x, self.y, self.w, self.h)
            else:
                (areaX, areaY, w, h) = self._getPlayingFieldCoord(img)
        self.moves += 1
        winX += areaX
        winY += areaY
        moveX = winX + 12 + (52*(x)) + 26
        moveY = winY+ 12 + (52*(y)) + 26
        pyautogui.moveTo(moveX,moveY)
        if direction == "U":
            pyautogui.drag(0, -50)
        elif direction == "D":
            pyautogui.drag(0, 50)
        elif direction == "R":
            pyautogui.drag(50, 0)
        else:
            pyautogui.drag(-50, 0)

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
