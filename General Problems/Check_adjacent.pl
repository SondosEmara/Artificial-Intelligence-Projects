adjacent( X, Y, [X,Y|_]).
adjacent( X, Y, [H1,H2|T]):-
	adjacent(X, Y, [H2|T]).
