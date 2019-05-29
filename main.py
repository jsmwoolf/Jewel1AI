import cv2
from Jewel1Env import Jewel1Env
from Jewel1RB import Jewel1RB
import pytesseract
import time
import numpy as np
import random

def showImage(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)

env = Jewel1Env()
env.launchGame()
env.handleTitleScreen()
time.sleep(2)
agent = Jewel1RB()
while True:
    canMakeMove = False
    while not canMakeMove:
        board = env.getPlayingFieldInfo()
        print(board)
        canMakeMove = agent.isBoardAvailable(board)
    moves = agent.processBoard(board)
    if len(moves) == 0:
        continue
    theMove = random.choice(moves)
    print("Chose move: {}".format(theMove))
    env.makeMove(int(theMove[1]), int(theMove[3]), theMove[-1])
    time.sleep(.5)
