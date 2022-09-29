
from GameStrategy import *


def drawBoard(currentBoardMatrix):
    for i in range(len(currentBoardMatrix)):
        print(i, " ", end=" ")
        for j in range(len(currentBoardMatrix[i])):
            if(currentBoardMatrix[i][j]==-1):
                print ("--",end=" ")
            else:
                print(currentBoardMatrix[i][j],end=" ")
        print("\n")

def WinOrNOt(currentPieces, currentTarget):

    ifWIN = True

    for onePiece in currentPieces:
        if onePiece not in currentTarget:
            ifWIN = False

    return ifWIN

#Start Point
def main():
    #The user will enter the game level status.
    choose=int(input("Please Enter the game level: 1 Easy 2 Mediam 3 Hard: "))
    if(choose==1):
        gameLevel=1
    elif(choose==2):
        gameLevel=3
    else:
        gameLevel=5

    #that function return the intial start matrix.
    currentBoardMatrix = getStartBorad()
    print("The intial Board")
    drawBoard(currentBoardMatrix)
    print("The Computer have a part 2,3 and 4 in game ,You Have part 1 and 5 and 6: ")

    human_1Piece, computer_2Piece, computer_3Piece, computer_4Piece, human_5Piece, human_6Piece = getStartPieces()
    human_1Target, computer_2Target, computer_3Target, computer_4Target, human_5Target, human_6Target = getTargetPieces()


    human1_NotAllowedPlaces,computer2_NotAllowedPlaces, computer3_NotAllowedPlaces,computer4_NotAllowedPlaces, human5_NotAllowedPlaces,human6_NotAllowedPlaces= \
        notAllowedplaces(human_1Piece, computer_2Piece, computer_3Piece, computer_4Piece, human_5Piece, human_6Piece, human_1Target,
                      computer_2Target, computer_3Target, computer_4Target, human_5Target, human_6Target)
    #first the computer part will be play first.
    #make the computerId to get the save the last computer id play.
    computerId = 2
    playerId=2
    computerWinCount=0
    humanWinCount=0

    while computerWinCount!=3 or humanWinCount!=3:
       # consider the pieces of the player of this playerId
       currentPieces = getCurrntSet(playerId, human_1Piece, computer_2Piece, computer_3Piece, computer_4Piece,
                               human_5Piece, human_6Piece)
       # identify homes of the player of this turn
       currentNotAllowedPlaces = getCurrentInvalidPlaces(playerId, human1_NotAllowedPlaces,
                                                    computer2_NotAllowedPlaces, computer3_NotAllowedPlaces,
                                                    computer4_NotAllowedPlaces, human5_NotAllowedPlaces,
                                                    human6_NotAllowedPlaces)

       # assign objective set of positions
       currentTarget = getCurrentTarget(playerId, human_1Target, computer_2Target, computer_3Target, computer_4Target,
                                human_5Target, human_6Target)

       # find all legal moves given a piece set of a player
       allPossibleMoves = getPossibleMoves(currentBoardMatrix, currentPieces, currentNotAllowedPlaces)
       if playerId==2 or playerId==3 or playerId==4:
           print("The Computer Will Play Now")
           bestMove = getBestMove(currentBoardMatrix, playerId,
                                      human_1Piece, computer_2Piece, computer_3Piece, computer_4Piece, human_5Piece,
                                      human_6Piece,gameLevel)
           print("The computer Move: ", bestMove)
           # do the best move
           currentBoardMatrix, currentPieces = doMoveAlgo(currentBoardMatrix, bestMove, currentPieces)
           print("The new currentBoardMatrix after the computer play")
           drawBoard(currentBoardMatrix)
           human_1Piece, computer_2Piece, computer_3Piece, computer_4Piece, human_5Piece, human_6Piece = \
               updatePieces(currentPieces, playerId, human_1Piece, computer_2Piece, computer_3Piece, computer_4Piece,
                                 human_5Piece, human_6Piece)

           ifWin = WinOrNOt(currentPieces, currentTarget)
           if ifWin:
               computerWinCount=computerWinCount+1
               print("The computer Part ",playerId," Is win ")

           #Turn to another player side
           print("Now You can Play")
           playerId = int(input("Choose which part will be move it from (1 or 6 or 5 ) : "))
       else:

           print("The all moves of the part ",playerId)
           print("The moves the first value in list is from piece and the second elemet is to piece")
           print(allPossibleMoves)
           index=int(input("Choose which piece would need to move it by choose matrix index start with 0: "))


           best_move=allPossibleMoves[index]
           currentBoardMatrix, currentPieces = doMoveAlgo(currentBoardMatrix, best_move, currentPieces)
           human_1Piece, computer_2Piece, computer_3Piece, computer_4Piece, human_5Piece, human_6Piece = \
               updatePieces(currentPieces, playerId, human_1Piece, computer_2Piece, computer_3Piece, computer_4Piece,
                                 human_5Piece, human_6Piece)

           print("The new currentBoardMatrix after the play")
           drawBoard(currentBoardMatrix)

           ifWin = WinOrNOt(currentPieces, currentTarget)
           if ifWin:
               humanWinCount=humanWinCount+1
               print("In Part ", playerId, " Is win ")

           # Turn to another computer side choose computer part.

           #print (computerId)
           if(computerId==4):
                #print("okkkkk")
                computerId=2
                playerId=2
           else:
               playerId = computerId + 1
               computerId=computerId+1

           #playerId=random.randint(2,4)

    if(computerWinCount==3):
          print("In the final Play the computer will won")
    elif(humanWinCount==3):
          print("You Now Win ")
if __name__ == '__main__':
    main()