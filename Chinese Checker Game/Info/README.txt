Programming Language :
  *Use Python
  
  
Project Run:
  *we use the import numpy and install  it from cmd command (pip install numpy).
  *using site-packages that contain the numpy.
  

Explain Some Points:

	  *First user take the game level (Easy,Mediam or Hard) -->This value will be pass to the function getBestMove as gameLevel(Depth)
	  *We assume that the computer have 3 colors parts -->P2,P3,P4.
	  *P2-->Yellow part,P3-->Orange part,P4-->Red part.
	  *when the computer will play we assume that have 3 parts acts as 3 players (P2,P3,P4)
	   when play will computer first choose what is the part will play
	   Choose through EX: the first choose the Player2 and second choose player3 and third choose Player4 and fourth 
	   return to choose Player1 again and go on.
   
	   *We assume the human(player) have there parts p1,p5,p6
	   *P1-->Green,P5-->purble,P6-->Blue.
	   *when the human(Player) will play we will show the star shape in the console by calling drawBoard Function.
	   *Human(Player) will first choose which part will be choose from it.
		part (1,5or6) and choose the part number then show the all possible moves for every piece in that part.
		using format [[From_Piece_Location_InMatrix],[To_Piece_Location_InMatrix]]
		and will choose the which move will make it by enter the row number index in matrix 
		Ex: the choose first move in matrix -->enter 0
			The choose second move in matrix -->enter 1
		*After make a move ,then show the board again after implement the move.
		
		*In the alpha beta algorithm we will make copy of the board because make a new board with the new move 
	    and when make bactracking and use the copy of the board to make new move and go to another path
		because the algorithm go depth and make backtracking to get other possible moves paths .
		
		*the depth of the alpha beta Algorithm to reach the utility depend on the game level (Easy -->1 and Mediam-->3 and hard-->5)


UtilityFunction:
 
        *Computer have (P2,P3,P4)
		*Human (Player) have (P1,P5,P6)

        *Algorithm we will make each player have a part color (pieces) the pieces is the locations of format (i,j) from the matrixBoard Location.
		*and we have the Target pieces in each player becuase 
		 each player represent pieces of specific part color and each player have a specific target pieces to reach it
		 EX:Computer when take part(Player4) the player pieces is red pieces location in the matrix
		    Target of the ComputerPart4 -->Is to reach to the locations Of Green pieces in the matrix.
			Red-->To Green.
			
			
		 and we have not allowed pieces for each player that represent 
		 Ex:if the computer will choose the part Red to move specific piece in it(choose the move using best Move)
		    the all possible new moves should not in any part of Any color except the green part(Because that is the target)
			new Move not in in any part Color -->like (Purple or blue or orange or yellow) intial(Start board places).
			but in the internal shape places.
			
			
		*So each playerId have a pieces,notAllowedPlaces and target.
        *Because of for each player have CurrentPieces Position in matrix , and targetpieces the target Locatins in matrix
		
        *we will calculate the UtilityFunction by 
            *For each player (Represent a color) get the target and currnt pieces.
			  get the total distince between the pieces and the target by using the law to get the distice between two points.
			  Ex:piece1 -->[i,j] location in matrix,
			     Target1-->[i0,j0] location in matrix 
				 Get the distince sqrt ((i0-i)*(i0-i)+(j0-j)(j0-j))
				 For all pieces and Targets add each Distance to totalDistance.
		    *Repeat the previous step untill we make all players.
			
			*final after repeat players we have:
			*Player1TotalDistance,Player2TotalDistance,Player3TotalDistance
			 Player4TotalDistance,Player5TotalDistance,Player6TotalDistance
			 
			 Beause the computer have (player 2,3,4) and Human have (Player 1,5,6)then 
			 computerDistance=Player2TotalDistance+Player3TotalDistance+Player4TotalDistance.
			 HumanDistance=Player1TotalDistance+Player5TotalDistance+Player6TotalDistance
			 
			 The final Utility Result is computerDistance-HumanDistance;