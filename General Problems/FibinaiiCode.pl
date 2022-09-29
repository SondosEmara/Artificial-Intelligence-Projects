%first we will put the base cases of the fib.
%base Cases.
fib(0,0):- !.
fib(1,1):- !.
fib(2,1):- !.

%the rule of the fibaniaii is fib(n)=fib(n-1)+fib(n-2).
%recusrion cases.
fib(N,Result):-N1 is N-1,N2 is N-2,
              fib(N1,Result1),fib(N2,Result2),
              Result is Result1+Result2.
             

