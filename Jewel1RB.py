import random
import copy
import pandas as pd

class Jewel1RB:
    def __init__(self):
        pass
    
    def verticalSearch(self, board):
        moves = []
        for x in range(8):
            occur = 0
            curColor = ""
            for y in range(8):
                if board[y][x] != curColor:
                    curColor = board[y][x]
                    if y+2 < 8 and board[y+2][x] == curColor:
                        if x-1 >= 0 and board[y+1][x-1] == curColor:
                            moves.append("({},{}){}".format(x,y+1, "L"))
                        if x+1 < 8 and board[y+1][x+1] == curColor:
                            moves.append("({},{}){}".format(x,y+1, "R"))
                else:
                    if y-3 >= 0 and board[y-3][x] == curColor:
                        moves.append("({},{}){}".format(x, y-2, "U"))
                    if y+2 < 8 and board[y+2][x] == curColor:
                        moves.append("({},{}){}".format(x, y+1, "D"))
                    if y-2 >= 0 and x-1 >= 0 and board[y-2][x-1] == curColor:
                        moves.append("({},{}){}".format(x,y-2, "L"))
                    if y-2 >= 0 and x+1 < 8 and board[y-2][x+1] == curColor:
                        moves.append("({},{}){}".format(x,y-2, "R"))
                    if y+1 < 8 and x-1 >= 0 and board[y+1][x-1] == curColor:
                        moves.append("({},{}){}".format(x,y+1, "L"))
                    if y+1 < 8 and x+1 < 8 and board[y+1][x+1] == curColor:
                        moves.append("({},{}){}".format(x,y+1, "R"))
                    curColor = ""
        return moves

    def horizontalSearch(self, board):
        moves = []
        for y in range(8):
            occur = 0
            curColor = ""
            for x in range(8):
                if board[y][x] != curColor:
                    curColor = board[y][x]
                    if x+2 < 8 and board[y][x+2] == curColor:
                        if y-1 >= 0 and board[y-1][x+1] == curColor:
                            moves.append("({},{}){}".format(x+1,y, "U"))
                        if y+1 < 8 and board[y+1][x+1] == curColor:
                            moves.append("({},{}){}".format(x+1,y, "D"))
                else:
                    if x-3 >= 0 and board[y][x-3] == curColor:
                        moves.append("({},{}){}".format(x-2, y, "L"))
                    if x+2 < 8 and board[y][x+2] == curColor:
                        moves.append("({},{}){}".format(x+1, y, "R"))
                    if y-1 >= 0 and x-2 >= 0 and board[y-1][x-2] == curColor:
                        moves.append("({},{}){}".format(x-2, y, "U"))
                    if y-1 >= 0 and x+1 < 8 and board[y-1][x+1] == curColor:
                        moves.append("({},{}){}".format(x+1, y, "U"))
                    if y+1 < 8 and x-2 >= 0 and board[y+1][x-2] == curColor:
                        moves.append("({},{}){}".format(x-2, y, "D"))
                    if y+1 < 8 and x+1 < 8 and board[y+1][x+1] == curColor:
                        moves.append("({},{}){}".format(x+1, y, "D"))
                    curColor = ""
        return moves

    def isBoardAvailable(self, board):
        for x in range(8):
            for y in range(8):
                if board[x][y] == "N/A":
                    return False
        return True
    
    def printBoard(self, board):
        for y in range(8):
                print(board[y][:])

    def processBoard(self, board):
        moves = []
        for move in self.verticalSearch(board):
            moves.append(move)
        for move in self.horizontalSearch(board):
            moves.append(move)
        return moves

    def _getMatchType(self, board, x, y, d):
        theType = ""
        c = ""
        ways = {1: 0, 2: 0, 3: 0}
        print("Getting move for ({}, {})".format(x, y))
        # Get the number of a color gem in a consecutive line
        if d == "U":
            c = board[y-1][x]
            for i in range(1,3):
                # Down
                if y+i < 8 and board[y+i][x] == c:
                    if i == 2 and ways[2] == 0:
                        continue
                    ways[2] = i
                # Right
                if x+i < 8 and board[y][x+i] == c:
                    if i == 2 and ways[3] == 0:
                        continue
                    ways[3] = i
                # Left
                if x-i >= 0 and board[y][x-i] == c:
                    if i == 2 and ways[1] == 0:
                        continue
                    ways[1] = i
        elif d == "D":
            c = board[y+1][x]
            for i in range(1,3):
                # Up
                if y-i >= 0 and board[y-i][x] == c:
                    if i == 2 and ways[2] == 0:
                        continue
                    ways[2] = i
                # Right
                if x+i < 8 and board[y][x+i] == c:
                    if i == 2 and ways[3] == 0:
                        continue
                    ways[3] = i
                # Left
                if x-i >= 0 and board[y][x-i] == c:
                    if i == 2 and ways[1] == 0:
                        continue
                    ways[1] = i
        elif d == "L":
            c = board[y][x-1]
            for i in range(1,3):
                # Down
                if y+i < 8 and board[y+i][x] == c:
                    if i == 2 and ways[1] == 0:
                        continue
                    ways[1] = i
                # Up
                if y-i >= 0 and board[y-i][x] == c:
                    if i == 2 and ways[3] == 0:
                        continue
                    ways[3] = i
                # Right
                if x+i < 8 and board[y][x+i] == c:
                    if i == 2 and ways[2] == 0:
                        continue
                    ways[2] = i
        else:
            c = board[y][x+1]
            for i in range(1,3):
                # Down
                if y+i < 8 and board[y+i][x] == c:
                    if i == 2 and ways[1] == 0:
                        continue
                    ways[1] = i
                # Up
                if y-i >= 0 and board[y-i][x] == c:
                    if i == 2 and ways[3] == 0:
                        continue
                    ways[3] = i
                # Left
                if x-i >= 0 and board[y][x-i] == c:
                    if i == 2 and ways[2] == 0:
                        continue
                    ways[2] = i
        if ways[1] == 2 and ways[2] == 2 and ways[3] == 2:
            theType = "3W"
        elif ways[1] > 0 and ways[3] > 0 and ways[2] == 2:
            theType = "T"
        elif (ways[1] == 2 or ways[3] == 2) and ways[2] == 2:
            theType = "L"
        elif ways[1] == 2 and ways[3] == 2:
            theType = "5M"
        elif (ways[1] == 2 and ways[3] == 1) or (ways[1] == 1 and ways[3] == 2):
            theType = "4M"
        else:
            theType = "3M"
        return theType
        
    def checkDoubleMove(self, moves):
        doubles = []
        for move in moves:
            x = int(move[1])
            y = int(move[3])
            d = move[-1]
            if d == "R":
                x += 1
                d = "L"
            elif d == "L":
                x -= 1
                d = "R"
            elif d == "U":
                y -= 1
                d = "D"
            else:
                y += 1
                d = "U"
            newPos = "({},{}){}".format(x, y, d)
            if newPos in moves:
                doubles.append(move)
        return doubles
    
    def predictAfterMove(self, move, board):
        d = move[-1]
        x = int(move[1])
        y = int(move[3])
        color = None
        xRange = []
        yRange = []
        if d == "R":
            color = board[y][x + 1]
            board[y][x + 1] = board[y][x]
            board[y][x] = color
            if x-2 >= 0 and board[y][x-1] == color and board[y][x-2] == color:
                xRange = [x-2, x-1, x]
            else:
                xRange.append(x)
            yRange.append(y)
            # Handle vertical range
            for i in range(1, 3):
                if y+i < 8 and board[y+i][x] == color and board[(y+i)-1][x] == color:
                    yRange.append(y+i)
                if y-i >= 0 and board[y-i][x] == color and board[(y-i)+1][x] == color:
                    yRange.append(y-i)
                
        elif d == "L":
            color = board[y][x - 1]
            board[y][x - 1] = board[y][x]
            board[y][x] = color
            if x+2 < 8 and board[y][x+1] == color and board[y][x+2] == color:
                xRange = [x+2, x+1, x]
            else:
                xRange.append(x)
            yRange.append(y)
            # Handle vertical range
            for i in range(1, 3):
                if y+i < 8 and board[y+1][x] == color and board[(y+i)-1][x] == color:
                    yRange.append(y+i)
                if y-i >= 0 and board[y-i][x] == color and board[(y-i)+1][x] == color:
                    yRange.append(y-i)

        elif d == "U":
            color = board[y - 1][x]
            board[y-1][x] = board[y][x]
            board[y][x] = color
            if y+2 < 8 and board[y+1][x] == color and board[y+2][x] == color:
                yRange = [y+2, y+1, y]
            else:
                yRange.append(y)
            xRange.append(x)
            # Handle vertical range
            for i in range(1, 3):
                if x+i < 8 and board[y][x+i] == color and board[y][(x+i)-1] == color:
                    xRange.append(x+i)
                if x-i >= 0 and board[y][x-i] == color and board[y][(x-i)-1] == color:
                    xRange.append(x-i)
        else:
            color = board[y + 1][x]
            board[y + 1][x] = board[y][x]
            board[y][x] = color
            if y-2 >= 0 and board[y-1][x] == color and board[y-2][x] == color:
                yRange = [y-2, y-1, y]
            else:
                yRange.append(y)
            xRange.append(x)
            # Handle vertical range
            for i in range(1, 3):
                if x+i < 8 and board[y][x+i] == color and board[y][(x+i)-1] == color:
                    xRange.append(x+i)
                if x-i >= 0 and board[y][x-i] == color and board[y][(x-i)-1] == color:
                    xRange.append(x-i)
        # Sort the ranges
        xRange.sort()
        yRange.sort()
        for xCol in xRange:
            space = (yRange[-1] - yRange[0]) + 1
            curY = yRange[0] - 1
            while curY >= 0:
                board[curY + space][xCol] = board[curY][xCol]
                board[curY][xCol] = 'N/A'
                curY -= 1
        return board
    
    def getBestMove(self, board):
        moves = self.processBoard(board)
        doubles = self.checkDoubleMove(moves)
        moveData = {"move": [], "type": [], "double": [], "reaction":[]}
        for move in moves:
            theType = self._getMatchType(
                board, 
                int(move[1]), 
                int(move[3]),
                move[-1]
            )
            isDouble = move in doubles
            afterBoard = self.predictAfterMove(move, copy.deepcopy(board))
            #self.printBoard(afterBoard)
            cascadeAmount = 0
            for x in range(8):
                for y in range(6):
                    if afterBoard[y][x] == 'N/A':
                        continue
                    if afterBoard[y][x] == afterBoard[y+1][x] and afterBoard[y+1][x] == afterBoard[y+2][x]:
                        cascadeAmount += 1
            for y in range(8):
                for x in range(6):
                    if afterBoard[y][x] == 'N/A':
                        continue
                    if afterBoard[y][x] == afterBoard[y][x+1] and afterBoard[y][x+1] == afterBoard[y][x+2]:
                        cascadeAmount += 1
            moveData['move'].append(move)
            moveData['type'].append(theType)
            moveData['double'].append(isDouble) 
            moveData['reaction'].append(cascadeAmount)
        matchOrdering = ["3W", "T", "L", "5M", "4M", "3M"]
        moveInfo = pd.DataFrame(moveData, columns=["move", "type", "double", "reaction"])

        moveInfo.type = moveInfo.type.astype("category")
        moveInfo.type.cat.set_categories(matchOrdering, inplace=True)

        moveInfo.sort_values(["type", "double"], ascending=[True, False], inplace=True)
        print(moveInfo.head(len(moveInfo)))
        bestMove = moveInfo.head(1).reset_index(drop=True)["move"][0]
        
        return bestMove
        