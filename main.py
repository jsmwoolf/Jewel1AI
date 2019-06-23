import cv2
from Jewel1Env import Jewel1Env
from Jewel1RB import Jewel1RB
import time
import numpy as np
import random

def showImage(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)

#lowRange = 60
#upperRange = 225
#white = cv2.inRange(cv2.imread("Board Incorrect Classify.png"),np.array([128, 128, 0]), np.array([225, 225,0]))
#showImage("White", white)
#exit()
env = Jewel1Env()
env.launchGame()
env.handleTitleScreen()
time.sleep(3)
agent = Jewel1RB()
board = ""
imageNumber = 0
while True:
    canMakeMove = False
    previousBoard = "1"
    while not canMakeMove and previousBoard != board:
        previousBoard = board
        board = env.getPlayingFieldInfo()
        canMakeMove = agent.isBoardAvailable(board)
    print(board)
    moves = agent.processBoard(board)
    if len(moves) == 0:
        continue
    theMove = agent.getBestMove(board)
    #cv2.imwrite("moves/{}.png".format(imageNumber), env.getPlayingField())
    print("Chose move #{}: {}".format(imageNumber,theMove))
    imageNumber += 1
    time.sleep(.25)
    env.makeMove(int(theMove[1]), int(theMove[3]), theMove[-1])
    time.sleep(1)
