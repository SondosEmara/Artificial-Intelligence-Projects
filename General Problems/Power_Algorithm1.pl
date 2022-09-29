
%algorithm 2^3==2*2*2.
%base case
power(Base,1,Base):- !.

%Recurcion Cases.
power(Base,Power,Result):-
     P1 is Power-1,
     power(Base,P1,Result1),
     Result is Base*Result1.


             


