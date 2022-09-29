%Base Case.
power(Base,1,Base):- !.

%Recusrion case case 2 if the power is odd.
power(Base,Power,Result):-
           not(0 is Power mod 2),
           P is floor(Power/2),
           power(Base,P,Output1),
           power(Base,P,Output2),
           Result is Base*Output1*Output2.


%Recursion Case. case 1 if the power is even.
power(Base,Power,Result):-
           0 is Power mod 2,
           %should convert the float to int.(Power/2)
           P is floor(Power/2),
           power(Base,P,Output1),
           power(Base,P,Output2),
           Result is Output2*Output1.


