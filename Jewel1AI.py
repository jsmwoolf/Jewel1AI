# This class holds information about our bot playing Bejeweled 1 game.
# Please note that this code will only support the Windows platform.
import cv2
import pyautogui
import os
import urllib.request as urllib
import win32gui
import time
import numpy as np

class Jewel1AI:
    # Holds the class information about the AI
    def __init__(self):
        self.hwnd = 0

    def getWindowShot(self):
        rect = win32gui.GetWindowRect(self.hwnd)
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y
        img = pyautogui.screenshot(region=(x, y, w, h))
        return np.array(img) 
        # Convert RGB to BGR 
        #open_cv_image = open_cv_image[:, :, ::-1].copy()s

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
