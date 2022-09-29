
from Players import *
import math
import copy
import random


#The gameLevel will be input paramter to know which level the user need (EASY Or Hard or mediam)
#act the playerId2,3,4 --> will be belong to computer
#act the playerId1,6,5-->will be belong to humanplayerId
def getBestMove(currentBoard,playerIdId, human_1Piece, computer_2Piece, computer_3Piece,
                   computer_4Piece, human_5Piece, human_6Piece,gameLevel):

        #Get all target which part will reach to another part.
        humanTarget_1, computerTarget_2, computerTarget_3, computerTarget_4, humanTarget_5, humanTarget_6 = getTargetPieces()

        #Get all not allowed places (that is not allowed for each playerId).
        human_NotAllowedPlaces_1, computer_NotAllowedPlaces_2, computer_NotAllowedPlaces_3, computer_NotAllowedPlaces_4, human_NotAllowedPlaces_5, human_NotAllowedPlaces_6 = \
        notAllowedplaces(human_1Piece, computer_2Piece, computer_3Piece, computer_4Piece, human_5Piece, human_6Piece, humanTarget_1,
                          computerTarget_2, computerTarget_3, computerTarget_4, humanTarget_5, humanTarget_6)

        #Call the alpaha beta to make the algorithm.
        s,bestMove = makeAlphaBeta(currentBoard,gameLevel, playerIdId,human_1Piece, computer_2Piece, computer_3Piece,
                   computer_4Piece, human_5Piece, human_6Piece,humanTarget_1, computerTarget_2, computerTarget_3, computerTarget_4, humanTarget_5, humanTarget_6,human_NotAllowedPlaces_1, computer_NotAllowedPlaces_2, computer_NotAllowedPlaces_3, computer_NotAllowedPlaces_4, human_NotAllowedPlaces_5, human_NotAllowedPlaces_6,-80000,80000)
        return bestMove

def makeAlphaBeta(currentBoard, gameLevel, playerId, human_1Pieces, computer_2Pieces, computer_3Pieces, computer_4Pieces, human_5Pieces,
              human_6Pieces,humanTarget_1, computerTarget_2, computerTarget_3, computerTarget_4, humanTarget_5, humanTarget_6,human_NotAllowedPlaces_1, computer_NotAllowedPlaces_2, computer_NotAllowedPlaces_3, computer_NotAllowedPlaces_4, human_NotAllowedPlaces_5, human_NotAllowedPlaces_6 , a, b):

    #make copy to save the board because when make backtracking get the correct current board in that time.
    boardMatrixFirstCopy = currentBoard[:][:]

    #Chcek Game level --->if reach to zero that is mean we will reach to utility function (reach to the end of the tree of one path.)
    if gameLevel == 0:
        utilityValue = getUtility( human_1Pieces,computer_2Pieces, computer_3Pieces, computer_4Pieces,
                                            human_5Pieces, human_6Pieces,humanTarget_1, computerTarget_2, computerTarget_3, computerTarget_4, humanTarget_5, humanTarget_6)
        return utilityValue, None

    #get the current pices of the current playerId play (Computer or Human)
    currentPieces = getCurrntSet(playerId, human_1Pieces, computer_2Pieces, computer_3Pieces, computer_4Pieces, human_5Pieces, human_6Pieces)

    # get the current pices Target of the current playerId play (Computer or Human)
    currentTarget = getCurrentTarget(playerId, humanTarget_1, computerTarget_2, computerTarget_3, computerTarget_4,
                             humanTarget_5, humanTarget_6)

    # get the current pices not allowed places of the current playerId play (Computer or Human)
    currentNotAllowedPlaces = getCurrentInvalidPlaces(playerId, human_NotAllowedPlaces_1, computer_NotAllowedPlaces_2, computer_NotAllowedPlaces_3,
                                             computer_NotAllowedPlaces_4, human_NotAllowedPlaces_5, human_NotAllowedPlaces_6)

    #Get all moves of that current picess -->belong to playerId.
    #possibleMoves is like matrix ,
    #ex:the first row is consider to [[fromPices][ToPices]] to know the move from to action when make the move.
    possibleMoves = getPossibleMoves(boardMatrixFirstCopy, currentPieces, currentNotAllowedPlaces)

    utilityValues = []
    totalMoves = []

    #take each move from all possible moves and make the move and intiallize new board after make the move
    if playerId == 2 or playerId == 3 or playerId == 4:
        for oneMove in possibleMoves:
                    #the computer will play with there playerId (2,3,4)
                    #and assume the computer is the Max Part (Alpha)
                    #So when make change the alpha --->change if the part is computer playerId.
                    boardMatrixSecondCopy = copy.copy(boardMatrixFirstCopy)
                    newMatrixBoard, newCurrentPieces = doMoveAlgo(boardMatrixSecondCopy, oneMove, currentPieces)

                    #updtae the current pices after make move by remove the old Piece Index and append new Piece Index
                    #Updtae the board matrix to get new board after the move.
                    human_1Pieces, computer_2Pieces, computer_3Pieces, computer_4Pieces, human_5Pieces, human_6Pieces = \
                        updatePieces(newCurrentPieces, playerId, human_1Pieces, computer_2Pieces, computer_3Pieces, computer_4Pieces,
                                          human_5Pieces, human_6Pieces)

                    #change the playerId to human -->Human belong to (1,4,5)playerIds Pieces.
                    #so get random between this numbers.
                    humanPlayId = random.randint(4,5)
                    #call again the makeAlphaBeta to go to the more depth untill we reach to utility function
                    #then make backtracking.
                    oneUtilityValue,s = makeAlphaBeta(newMatrixBoard, gameLevel - 1, humanPlayId, human_1Pieces, computer_2Pieces,
                                                 computer_3Pieces, computer_4Pieces, human_5Pieces, human_6Pieces,
                                                     humanTarget_1, computerTarget_2, computerTarget_3, computerTarget_4, humanTarget_5,
                                                     humanTarget_6, human_NotAllowedPlaces_1, computer_NotAllowedPlaces_2, computer_NotAllowedPlaces_3,
                                                     computer_NotAllowedPlaces_4, human_NotAllowedPlaces_5, human_NotAllowedPlaces_6,a,b)

                    #append the one utility function in all utilityis that belong to the Max Part.
                    #because the end will choose the max from the list.(when make backtracking)
                    #total moves to choose the end the best move so we should store it.
                    utilityValues.append(oneUtilityValue)
                    totalMoves.append(oneMove)

                    #Compare between the result oneUtilityValue to the alpha to update the alpha
                    #take max because that is alpha and we in the computer playerId (Max)
                    a = max(oneUtilityValue, a)

                    #make break because it not important to continue with other paths becuse that still the same number of alpa not change
                    if b <= a:
                        break

        #after end the for loop that mean we reach in the end and collect in array(utilityValues) all the values of all moves that is the max make.
        #so we choose a max from all values and get the index of the that value
        #get the move of corresponding to that utility value.
        #choose the max becuse we in the computer part.
        maxIndex = utilityValues.index(max(utilityValues))
        bestMove = totalMoves[maxIndex]
        return utilityValues[maxIndex],bestMove

    #the human Part
    elif(playerId==1 or playerId==5 or playerId==6):

        for oneMove in possibleMoves:
            #copy the board becuase when make bactracking work on the old board not the new board after make previous move.
            boardMatrixSecondCopy = copy.copy(boardMatrixFirstCopy)
            newMatrixBoard, newCurrentPieces = doMoveAlgo(boardMatrixSecondCopy, oneMove, currentPieces)

            human_1Pieces, computer_2Pieces, computer_3Pieces, computer_4Pieces, human_5Pieces, human_6Pieces = \
                updatePieces(newCurrentPieces, playerId, human_1Pieces, computer_2Pieces, computer_3Pieces, computer_4Pieces,
                                  human_5Pieces, human_6Pieces)

            #beacuse the computer have there parts -->acts the computer will play with 3 playerIds(2,3,4).
            computerPlayId = random.randint(2,4)

            oneUtilityValue,s = makeAlphaBeta(newMatrixBoard, gameLevel - 1, computerPlayId, human_1Pieces, computer_2Pieces,
                                         computer_3Pieces, computer_4Pieces, human_5Pieces, human_6Pieces,humanTarget_1, computerTarget_2, computerTarget_3, computerTarget_4, humanTarget_5, humanTarget_6,human_NotAllowedPlaces_1, computer_NotAllowedPlaces_2, computer_NotAllowedPlaces_3, computer_NotAllowedPlaces_4, human_NotAllowedPlaces_5, human_NotAllowedPlaces_6 , a, b)

            #save the utility values to make bactracking correct
            #bactracking From bottom to top
            utilityValues.append(oneUtilityValue)
            totalMoves.append(oneMove)

            #choose the min because we in the human part (playerIdId)
            b = min(oneUtilityValue, b)
            if b <= a:
                break

        #choose the min of all list to get the most move will be not won the computer.
        #when reach in computer part will choose the max.
        minIndex = utilityValues.index(min(utilityValues))
        minMove = totalMoves[minIndex]
        return utilityValues[minIndex], minMove




def getUtility(playerPices1,playerPices2,playerPices3,playerPices4,playerPices5,playerPices6,
               playerTarget1,playerTarget2,playerTarget3,playerTarget4,playerTarget5,playerTarget6):
     #the computer belong to (2,3,4)distinces
     #the player belong to (1,5,6) distices
    distanceP1=getDistance(playerPices1,playerTarget1)
    distanceP2 = getDistance(playerPices2, playerTarget2)
    distanceP3 = getDistance(playerPices3, playerTarget3)
    distanceP4 = getDistance(playerPices4, playerTarget4)
    distanceP5 = getDistance(playerPices5, playerTarget5)
    distanceP6 = getDistance(playerPices6, playerTarget6)

    sumComputerDistince=distanceP2+distanceP3+distanceP4
    sumHumanDistince=distanceP1+distanceP5+distanceP6

    #Get Difference between them
    return sumComputerDistince-sumHumanDistince


#get the ditsince between the currentplayerPicess and the playertarget.
def getDistance(playerPices,playerTarget):
    totalDistince=0
    for i in range (10):
        [row1,col1]=playerPices[i]
        [row2, col2] =playerTarget[i]
        totalDistince=totalDistince+math.sqrt((row2-row1)*(row2-row1)+(col2-col1)*(col2-col1))

    return totalDistince


