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
        
            
    def getBestMove(self, board):
        moves = self.processBoard(board)
        moveType = {}
        for move in moves:
            theType = self._getMatchType(
                board, 
                int(move[1]), 
                int(move[3]),
                move[-1]
            )
            if theType not in moveType:
                moveType[theType] = [move]
            else:
                moveType[theType].append(move)
        return moveType
        