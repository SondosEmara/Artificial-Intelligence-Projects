
%----------------Common Functions to use in Problem 1 and 2-------------

%-------------------     addListToOpen        ---------------------------
addListToOpen(Children,[],Children).
addListToOpen(L, [H|Open], [H|NewOpen]):-
		addListToOpen(L, Open, NewOpen).
		
		

%------------------     InlIST(ifContain)      ---------------------------
inList(H, [H|_]).
inList(H, [_|T]) :- 
    inList(H, T).
	
	
%---------------      JoinLists(like append)   ---------------------------
% Takes two lists and appends them
joinLists([], L2, L2).
joinLists([H|T], L2, [H|R]):-
    joinLists(T, L2, R).
	
%------------------Remove From List---------
removeFromList(_, [], []):-!.
removeFromList(H, [H|T], V):-
	!, removeFromList(H, T, V).
removeFromList(H, [H1|T], [H1|T1]):-
	removeFromList(H, T, T1).
	
%-----------------Get Best----------------
getBestChild([Child], Child, []):-!.

%Returns the best child from the open list, and the rest of the open list.
getBestChild(Open, Best, RestOpen):-
	getBestChild1(Open, Best),
	removeFromList(Best, Open, RestOpen).

% Iterates through the open list to find the best child.
getBestChild1([State], State):-!.
getBestChild1([State|Rest], Best):-
	getBestChild1(Rest, Temp),
	getBest(State, Temp, Best).
	
%---------------Using In p1---------------
% Returns the smaller cost (best) between two states.
getBest([State, _, H1], [_, _, H2], [State, _, H1]) :-
H1 < H2,!.
getBest(_, [State, _, H2], [State, _, H2]).


%-----------------Using in p2-------------
getBest([State,H1],[_,H2],[State,H1]):-
H1<H2,!.
getBest(_,[State,H2],[State,H2]).

%--------------------------------Problem 1---------------------------------

/*
---------------------Problem 1 Using depth first search--------------------
THe idea make intial state is empty and make two moves
First Move is Include ,Second is not include.

save the first list as original data to iterate about that list element by element.
Goal -->Reach to [A,B,C] there numbers thier summations will reach the integer goal.
the intial state is [[[],-1]]

%the -1 is intial index of intial state so make it -1 
becuase when incerease it by 1 that  mean we in the first element in original data input 
that is mean when incerease the-1 bewcome 0 -->
Possible move is add in new list the first element in originalData
or still not include the first element.
and repeat untill the open become empty.

original Data ex:[1,2,3]
the intial state is [[[],-1]] ,the childern will be [[1],0],[[],0]
when take the [[1],0] from open the childern will be [[1,2],1] and [[1],1]
moveing steps :include the elemnet to the list or not include.
*/



%-----------Main Predictae--------------------
threeSum(Intial,Goal,Output):-
	%the intial state is [[[],-1]]
	%-1 is Index
	write("\nThe Depth First Search Result\n\n"),
    depthFirst([[[],-1]],[],Intial,Goal,[],SaveFinal,Output),
	write("\nThe Greedy Search Result\n\n"),
	heuristic([], Goal, H),
    greedyAlgo([[[],-1,H]],[],Intial,Goal,[],SaveFinal,Output).
  
%-------------------depthFirst----------------
%Base Case when the Open reach to empty list
depthFirst([],C,_,_,_,SaveFinal,Output):-printFinalResult(SaveFinal,0,Output).

%OrginalData is always is the intial State.
depthFirst(Open,Closed,OrginalData,Goal,Out,SaveFinal,Output):-

   %remove the first element in open and but rest in RestOfOpen.
   removeFromOpen(Open, [State,Index], RestOfOpen),
   
   %Check the State list if its reach to goal or not 
   %Fisrt 0 is Sum ,Second 0 is iterator Count intial.
   %New is result
   checkReachGoal(Goal,0,0,State,Out,New),
   joinLists(SaveFinal,[New],NewFinal),
   
   %Get Childern to the state that after delete from open.
   getchildren(State,Index,OrginalData,Open,Children),
   
   %Update the Open List with rest+NewChildern.
   addListToOpen(RestOfOpen,Children , NewOpen),
   
   %update the Closed list by using [[State, Id] | Closed].
   depthFirst(NewOpen,[[State,Index] | Closed],OrginalData,Goal,Out,NewFinal,Output).


%--------------RemoveFromOpen-------------
removeFromOpen([State|RestOpen], State, RestOpen).


%----------------checkReachGoal-----------
%iterate to the list untill take 3 elements and check if sum ==Goal with base case.
checkReachGoal(Goal,Goal,3,_,Out,Out).
checkReachGoal(Goal,Sum,It,[Head|Tail],Out,N):-
    NewSum is Sum+Head,
	NewIt is It +1,
	joinLists(Out,[Head],NewList),
	checkReachGoal(Goal,NewSum,NewIt,Tail,NewList,N).
	
checkReachGoal(_,_,_,_,_,[]).	
	
	
%----------------GetChildern----------------
%include Element with list
move(List,Element,NewList):-
  joinLists(List,[Element],NewList).

getchildren(State,Index,OrginalData,Open,Children):-
 
    getLength(State,N,0),
	
	(
	    %Condition to check lenght because it is not important to get childern of lenght state >=3 .
	    ( N<3 )->
				NewIndex is Index+1,
				getElement(NewIndex,OrginalData,Element,0),!,
				move(State,Element,NewList),
				%[State,NewIndex] is the not include move.
				joinLists([],[[NewList,NewIndex],[State,NewIndex]],Children);
	
	
	    %else Condition(continue search).
		!
	).
	
getchildren(State,Index,OrginalData,Open,[]).	
		
%------------GetLength of the list------------
getLength([],N,N).
getLength([Head|Tail],N,It):-
  NewIt is It+1,
  getLength(Tail,N,NewIt).
  
	
%-----------printFinalResult-----------------
printFinalResult([],0,Out):-
    write("Output = "),write("false\n\n").
printFinalResult([Head|Tail],Flag,Output):-
  not((Head==[])),
  not(inList(Head,Tail)),!,
  write("Output= "),
  write(Head),
  write("\n"),
  printFinalResult(Tail,1,Output).
   
printFinalResult([Head|Tail],Flag,Output):-printFinalResult(Tail,Flag,Output).
printFinalResult([],1,_).


%-------------GetElement_InSpecificIndex-------
getElement(0,[Head|Tail],Head,0).
getElement(Index,[Head|Tail],Head,Index).
getElement(_,[],E,_):-fail.
getElement(Index,[Head|Tail],ELement,It):-
   NewIt is It+1,
   getElement(Index,Tail,ELement,NewIt).


%-------------Greedy------------------
greedyAlgo([],C,_,_,_,SaveFinal,Output):-printFinalResult(SaveFinal,0,Output).

greedyAlgo(Open,Closed,OrginalData,Goal,Out,SaveFinal,Output):-
   
   getBestChild(Open, [State, Index, H], RestOfOpen),
  
   checkReachGoal(Goal,0,0,State,Out,New),
   joinLists(SaveFinal,[New],NewFinal),
  
   getchildren(State,Index,H,Goal,OrginalData,Children),

   addListToOpen(RestOfOpen,Children , NewOpen),
   
   greedyAlgo(NewOpen,[[State,Index, H] | Closed],OrginalData,Goal,Out,NewFinal,Output).

%----------------GetChildern(Greedy)----------------

getchildren(State,Index,H,Goal,OrginalData,Children):-
    getLength(State,N,0),
	
	(
	    %Condition to check lenght because it is not important to get childern of lenght state >=3 .
	    ( N<3 )->
			NewIndex is Index+1,
			getElement(NewIndex,OrginalData,Element,0),!,
			move(State,Element,NewList),
			heuristic(NewList, Goal, H1),
			joinLists([],[[NewList,NewIndex, H1],[State,NewIndex,H]],Children);
			
	    %else Condition(continue search).
		!
	).
	
getchildren(State,Index,H,Goal,OrginalData,[]).	


%------------------------heuristic--------------------------
sumList([], R, R).

% Takes a list and returns its sum in R.
% S is initialized to 0 when the function is called.
sumList([H|T], S, R) :-
    S1 is S + H,
    sumList(T, S1, R).
    
% Returns the absolute value
absolute(X, X) :- 
    X >= 0, !.

absolute(X, X1) :-
    X < 0, 
    X1 is -X.


% Heuristic function based on the absolute value of the difference between 
% the goal and sum the current state (list).
% h(n) = absolute(sum(currentState-goal)).

heuristic(List, Goal, H) :-
    sumList(List, 0, Result),
    Difference is Result - Goal,
    absolute(Difference, R),
    H is R.
	





