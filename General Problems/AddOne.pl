addOne([],[]).
addOne([T1|L1],[T2|L2]):-
   ADD is T1+1,
   ADD==T2,
   addOne(L1,L2).
