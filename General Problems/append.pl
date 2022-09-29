%[] is empty list.
%Base case.
append([],List,List).

% the list in prolog can divde in two parts the first part is head and second is tail
% EX: if [1,2,3,4] in this list the head=1,Tail=[2,3,4].
%RL1 -- remainng of the list1
append([H|RL1],L2,[H|L3]):-append(RL1,L2,L3).