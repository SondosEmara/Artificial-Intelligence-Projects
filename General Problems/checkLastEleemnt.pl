ifLastElement( Element, List):-
	append( _, [Element], List).

%append( *List1, *List2, *List3), where List3 is the result of appending %List1 then List2
append( [], L, L).
append( [H|T], L2, [H|NT]):-
	append(T, L2, NT).
