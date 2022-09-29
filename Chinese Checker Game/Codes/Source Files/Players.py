import numpy as numbObj

#That Function will return the Board Matrix.
#The intiall Board when start program.
def getStartBorad():
    #Intiall Build matrix with number of rows =17 and number of columns=25.
    boardMatrix = numbObj.zeros((17, 25))

    #FILL all element of the boardMatrix matrix to -1
    #Because the -1 will be in the future the outer places of star shape
    #but intiall make all the boardMatrix values =-1.
    #To make it ease to print and know what is the internal in the shape and what is external in the shape.
    boardMatrix[:][:] = -1

    #The computer will have there parts (Player2 && 3&&4)
    #Fill the boardMatrix will be Take From Player1.
    boardMatrix[0][12] = 1
    boardMatrix[1][11] = 1
    boardMatrix[1][13] = 1
    boardMatrix[2][10] = 1
    boardMatrix[2][12] = 1
    boardMatrix[2][14] = 1
    boardMatrix[3][9] = 1
    boardMatrix[3][11] = 1
    boardMatrix[3][13] = 1
    boardMatrix[3][15] = 1

    # Fill the boardMatrix will be Take From Player2
    boardMatrix[4][18] = 2
    boardMatrix[4][20] = 2
    boardMatrix[4][22] = 2
    boardMatrix[4][24] = 2
    boardMatrix[5][19] = 2
    boardMatrix[5][21] = 2
    boardMatrix[5][23] = 2
    boardMatrix[6][20] = 2
    boardMatrix[6][22] = 2
    boardMatrix[7][21] = 2

    # Fill the boardMatrix will be Take From Player3
    boardMatrix[9][21] = 3
    boardMatrix[10][20] = 3
    boardMatrix[10][22] = 3
    boardMatrix[11][19] = 3
    boardMatrix[11][21] = 3
    boardMatrix[11][23] = 3
    boardMatrix[12][18] = 3
    boardMatrix[12][20] = 3
    boardMatrix[12][22] = 3
    boardMatrix[12][24] = 3

    # Fill the boardMatrix will be Take From Player4
    boardMatrix[13][9] = 4
    boardMatrix[13][11] = 4
    boardMatrix[13][13] = 4
    boardMatrix[13][15] = 4
    boardMatrix[14][10] = 4
    boardMatrix[14][12] = 4
    boardMatrix[14][14] = 4
    boardMatrix[15][11] = 4
    boardMatrix[15][13] = 4
    boardMatrix[16][12] = 4

    # Fill the boardMatrix will be Take From Player5
    boardMatrix[9][21 - 18] = 5
    boardMatrix[10][20 - 18] = 5
    boardMatrix[10][22 - 18] = 5
    boardMatrix[11][19 - 18] = 5
    boardMatrix[11][21 - 18] = 5
    boardMatrix[11][23 - 18] = 5
    boardMatrix[12][18 - 18] = 5
    boardMatrix[12][20 - 18] = 5
    boardMatrix[12][22 - 18] = 5
    boardMatrix[12][24 - 18] = 5

    # Fill the boardMatrix will be Take From Player6
    boardMatrix[4][18 - 18] = 6
    boardMatrix[4][20 - 18] = 6
    boardMatrix[4][22 - 18] = 6
    boardMatrix[4][24 - 18] = 6
    boardMatrix[5][19 - 18] = 6
    boardMatrix[5][21 - 18] = 6
    boardMatrix[5][23 - 18] = 6
    boardMatrix[6][20 - 18] = 6
    boardMatrix[6][22 - 18] = 6
    boardMatrix[7][21 - 18] = 6

    #Other Places is represtent the internall places of the star shape.
    #Allocate it to 0
    boardMatrix[4][8] = 0
    boardMatrix[4][10] = 0
    boardMatrix[4][12] = 0
    boardMatrix[4][14] = 0
    boardMatrix[4][16] = 0

    boardMatrix[5][7] = 0
    boardMatrix[5][9] = 0
    boardMatrix[5][11] = 0
    boardMatrix[5][13] = 0
    boardMatrix[5][15] = 0
    boardMatrix[5][17] = 0

    boardMatrix[6][6] = 0
    boardMatrix[6][8] = 0
    boardMatrix[6][10] = 0
    boardMatrix[6][12] = 0
    boardMatrix[6][14] = 0
    boardMatrix[6][16] = 0
    boardMatrix[6][18] = 0

    boardMatrix[7][5] = 0
    boardMatrix[7][7] = 0
    boardMatrix[7][9] = 0
    boardMatrix[7][11] = 0
    boardMatrix[7][13] = 0
    boardMatrix[7][15] = 0
    boardMatrix[7][17] = 0
    boardMatrix[7][19] = 0

    boardMatrix[7][5] = 0
    boardMatrix[7][7] = 0
    boardMatrix[7][9] = 0
    boardMatrix[7][11] = 0
    boardMatrix[7][13] = 0
    boardMatrix[7][15] = 0
    boardMatrix[7][17] = 0
    boardMatrix[7][19] = 0

    boardMatrix[8][4] = 0
    boardMatrix[8][6] = 0
    boardMatrix[8][8] = 0
    boardMatrix[8][10] = 0
    boardMatrix[8][12] = 0
    boardMatrix[8][14] = 0
    boardMatrix[8][16] = 0
    boardMatrix[8][18] = 0
    boardMatrix[8][20] = 0

    boardMatrix[9][5] = 0
    boardMatrix[9][7] = 0
    boardMatrix[9][9] = 0
    boardMatrix[9][11] = 0
    boardMatrix[9][13] = 0
    boardMatrix[9][15] = 0
    boardMatrix[9][17] = 0
    boardMatrix[9][19] = 0

    boardMatrix[10][6] = 0
    boardMatrix[10][8] = 0
    boardMatrix[10][10] = 0
    boardMatrix[10][12] = 0
    boardMatrix[10][14] = 0
    boardMatrix[10][16] = 0
    boardMatrix[10][18] = 0

    boardMatrix[11][7] = 0
    boardMatrix[11][9] = 0
    boardMatrix[11][11] = 0
    boardMatrix[11][13] = 0
    boardMatrix[11][15] = 0
    boardMatrix[11][17] = 0

    boardMatrix[12][8] = 0
    boardMatrix[12][10] = 0
    boardMatrix[12][12] = 0
    boardMatrix[12][14] = 0
    boardMatrix[12][16] = 0

    return boardMatrix

#Get start Piceces of each player
#The computer have 2,3,4
#The player have 1,5,6
def getStartPieces():

    computer_2 = [[4, 18], [4, 20], [4, 22], [4, 24], [5, 19], [5, 21], [5, 23], [6, 20], [6, 22], [7, 21]]
    computer_3 = [[9, 21], [10, 20], [10, 22], [11, 19], [11, 21], [11, 23], [12, 18], [12, 20], [12, 22], [12, 24]]
    computer_4 = [[13, 9], [13, 11], [13, 13], [13, 15], [14, 10], [14, 12], [14, 14], [15, 11], [15, 13], [16, 12]]
    player1_1 = [[0, 12], [1, 11], [1, 13], [2, 10], [2, 12], [2, 14], [3, 9], [3, 11], [3, 13], [3, 15]]
    player1_5 = [[9, 3], [10, 2], [10, 4], [11, 1], [11, 3], [11, 5], [12, 0], [12, 2], [12, 4], [12, 6]]
    player1_6 = [[4, 0], [4, 2], [4, 4], [4, 6], [5, 1], [5, 3], [5, 5], [6, 2], [6, 4], [7, 3]]

    return player1_1, computer_2, computer_3, computer_4, player1_5, player1_6


#getTargetPieces is each player will need to reach a specific target to know if it is win or not?
#The RedPices--->Go to Green and (Otherwise)
#The computer will take YELLOW and RED AND ORANGE
#The computer will act as 3 players in the Game that have:
#Player 2 is Yellow part
#Player 3 is Orange part
#Player 4 is Red part

#The PlayerHuman will act as 3 players in the Game that have:
#Player 1 is Green part
#Player 6 is Blue part
#Player 5 is purble part
def getTargetPieces():

    humanTarget1 = [[16, 12], [15, 11], [15, 13], [14, 10], [14, 14], [14, 12], [13, 9], [13, 15], [13, 13], [13, 11]]
    computerTarget2 = [[12, 0], [11, 1], [12, 2], [10, 2], [12, 4], [11, 3], [9, 3], [12, 6], [11, 5], [10, 4]]
    computerTarget3 = [[4, 0], [4, 2], [5, 1], [4, 4], [6, 2], [5, 3], [4, 6], [7, 3], [6, 4], [5, 5]]
    computerTarget4 = [[0, 12], [1, 13], [1, 11], [2, 14], [2, 10], [2, 12], [3, 15], [3, 9], [3, 11], [3, 13]]
    humanTarget5 = [[4, 24], [5, 23], [4, 22], [6, 22], [4, 20], [5, 21], [7, 21], [4, 18],  [5, 19], [6, 20]]
    humanTarget6 = [[12, 24], [12, 22], [11, 23], [12, 20], [10, 22], [11, 21], [12, 18], [9, 21], [10, 20], [11, 19]]
    return humanTarget1, computerTarget2, computerTarget3, computerTarget4, humanTarget5, humanTarget6


#for each player have a invaild places to assign in it
#For example if the red picess --> Green Picces target that is not allowed to the red picess to put in the places of the yellow or blue or purble.
def notAllowedplaces(human_1Pieces, computer_2Pieces, computer_3Pieces, computer_4Pieces, human_5Pieces, human_6Pieces, human_1Target, computer_2Target, computer_3Target, computer_4Target, human_5Target, human_6Target):

        p1IN = computer_2Pieces + computer_2Target + human_6Pieces+ human_6Target
        p2IN = human_1Pieces + human_1Target + human_6Pieces+ human_6Target
        p3IN = computer_2Pieces + computer_2Target + computer_4Pieces + computer_4Target
        p4IN = human_5Pieces + human_5Target + human_6Pieces + human_6Target
        p5IN = computer_4Pieces + computer_4Target + computer_3Pieces + computer_3Target
        p6IN = computer_4Pieces + computer_4Target + human_5Pieces + human_5Target
        return p1IN, p2IN, p3IN, p4IN, p5IN, p6IN

#To know which the picess of which player.(Curent Set)
def getCurrntSet(playerId, human_1Pieces, computer_2Pieces, computer_3Pieces, computer_4Pieces, human_5Pieces, human_6Pieces):

    currentSet = human_1Pieces

    if playerId == 1:
        currentSet = human_1Pieces
    elif playerId == 2:
        currentSet = computer_2Pieces
    elif playerId == 3:
        currentSet = computer_3Pieces
    elif playerId == 4:
        currentSet = computer_4Pieces
    elif playerId == 5:
        currentSet = human_5Pieces
    else:
        currentSet = human_6Pieces

    return currentSet

#Get Current Target of the Specific player Player Id
#Send all objective Traget in the paramter fnction.
def getCurrentTarget(playerId, human_1Target, computer_2Target, computer_3Target, computer_4Target, human_5Target, human_6Target):

    currentTarget = human_1Target

    if playerId == 1:
        currentTarget = human_1Target
    elif playerId == 2:
        currentTarget = computer_2Target
    elif playerId == 3:
        currentTarget = computer_3Target
    elif playerId == 4:
        currentTarget = computer_4Target
    elif playerId == 5:
        currentTarget = human_5Target
    else:
        currentTarget = human_6Target

    return currentTarget


#Get current Invalid places
def getCurrentInvalidPlaces(playerId, player1_invalid_home, player2_invalid_home, player3_invalid_home, player4_invalid_home, player5_invalid_home, player6_invalid_home):

    currrentNotAlllowed = player1_invalid_home

    if playerId == 1:
        currrentNotAlllowed = player1_invalid_home
    elif playerId == 2:
        currrentNotAlllowed = player2_invalid_home
    elif playerId == 3:
        currrentNotAlllowed = player3_invalid_home
    elif playerId == 4:
        currrentNotAlllowed = player4_invalid_home
    elif playerId == 5:
        currrentNotAlllowed = player5_invalid_home
    else:
        currrentNotAlllowed = player6_invalid_home

    return currrentNotAlllowed


#Update the set of the specific player
#and return player set after make update.
def updatePieces(newPieces, playerId, human_1Pieces, computer_2Pieces, computer_3Pieces, computer_4Pieces, human_5Pieces, human_6Pieces):

    if playerId == 1:
        human_1Pieces = newPieces
    elif playerId == 2:
        computer_2Pieces = newPieces
    elif playerId == 3:
        computer_3Pieces = newPieces
    elif playerId == 4:
        computer_4Pieces = newPieces
    elif playerId == 5:
        human_5Pieces = newPieces
    else:
        human_6Pieces = newPieces

    return human_1Pieces, computer_2Pieces, computer_3Pieces, computer_4Pieces, human_5Pieces, human_6Pieces



#Function to find all Moves.
#will get all moves from each piece From the pieces in spesific player.
def getPossibleMoves(boardMatrix,currntPieces,notAllowedPlaces):
    moves = []
    for onePiece in currntPieces:
        moves = getMovesForOnePiece(boardMatrix, onePiece, moves)

    #Beacuse the moves can be make invalid because the not allowed places.
    moves = deleteNotAllowedPlaces(moves, notAllowedPlaces)
    #return final moves.
    return moves

#Get all Possible Moves of one pices.
def getMovesForOnePiece(boardMatrix,onePiece,totalMoves):

    #it is possibleMoves in onePiece
    # onePiece is the have two location index from the boardMatrix(Location of row number,and location of column number).

    [row, col] = onePiece
    # that is moves can be valid or invalid moves.
    # so when make return we will check if it is vaild or not
    possibleMoves = []
    # case 1 -->increse the row and increase col
    if 0 <= (row+ 1) <= 16 and 0 <= (col + 1) <= 24:
        # append new move with the total result
        possibleMoves.append([row + 1, col + 1])

    # case 2 -->increse the row and decarese col
    if 0 <= (row + 1) <= 16 and 0 <= (col- 1) <= 24:
        possibleMoves.append([row + 1, col- 1])

    # case 3-->decarese the row and increase col
    if 0 <= (row - 1) <= 16 and 0 <= (col + 1) <= 24:
        possibleMoves.append([row - 1, col + 1])

    # case 4-->decarese the row and decarese col
    if 0 <= (row - 1) <= 16 and 0 <= (col- 1) <= 24:
        possibleMoves.append([row - 1, col- 1])

    #case 5-->incearse the row with 2 and col with 2
    if 0 <= (row+2) <= 16 and 0 <= (col +2) <= 24:
        # append new move with the total result
        possibleMoves.append([row + 2, col + 2])


    #check the moves valid or not.
    for i,j in possibleMoves:

        #Check if the place that will select is the value in matrix is empty or not.
        #Because it is not allowed to make move in place already in use.
        if boardMatrix[i][j] == 0:
            totalMoves.append([onePiece, [i,j]])

        #Not valid move of OnePice
        #choose another move.
        #be take it new move with any new move. but must check again if the new move is allowed or not.
        elif boardMatrix[i][j] > 0:
            x = i + (i -row)
            y = j + (j -col)
            if 0<=(x)<=16 and 0<=(y)<=24 and boardMatrix[x][y] ==0:
                totalMoves.append([onePiece, [x, y]])

    #One move in total moves is format [[FromPieceIndexOfmatrix],[ToPieceIndexOfmatrix]]
    #because that will be ease when select move to update the board with new move (ToPieceIndexOfmatrix) and change the value FromPieceIndexOfmatrix in matrix
    return totalMoves


#invalidPlace is places not allowed in moves matrix indexes
def deleteNotAllowedPlaces(moves, notAllowedPlaces):

    #the onemove contain[[From],[To]].
    totalMovesAfterFilter = []
    #check
    for oneMove in moves:
        toPiece = oneMove[1]
        #copy all moves that is allowed.
        if toPiece not in notAllowedPlaces:
            totalMovesAfterFilter.append(oneMove)

    return totalMovesAfterFilter


#Make move this function take board and update with the new move and update the picess with inculde new move.
#Each move have a [[FromIndex][ToIndex]]
def doMoveAlgo(currentBoard,oneMove,currentPieces):
    # From Index
    # the move contain [[from piece ],[to piece]]
    # from piece
    [fromRow, fromCol] = oneMove[0]

    # ToIndex(To piece).
    [toRow, toCol] = oneMove[1]

    # Update the board with new pices
    # FromIndex represent-->the oldmove
    # TOindex represent-->the newMove
    temp = currentBoard[fromRow][fromCol]
    currentBoard[fromRow][fromCol] = 0
    currentBoard[toRow][toCol] = temp

    # Updtae the currentPieces by remove the oldMove and insert new newMove
    # Copy all currentPieces to new except the oldMove
    oldPiece = [fromRow, fromCol]

    # iterate to all currentPieces and copy it but not copy the oldPiece
    newCurrentPieces = []
    for i in range(10):
        if (currentPieces[i] != oldPiece):
            newCurrentPieces.append(currentPieces[i])

    # append the new at the end of newCurrentPieces
    newCurrentPieces.append([toRow, toCol])
    return currentBoard, newCurrentPieces

