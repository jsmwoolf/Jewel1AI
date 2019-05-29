class Jewel1RB:
    def __init__(self):
        self.moves = {}
    
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
        self.moves = []
        for move in self.verticalSearch(board):
            self.moves.append(move)
        for move in self.horizontalSearch(board):
            self.moves.append(move)
        return self.moves
        