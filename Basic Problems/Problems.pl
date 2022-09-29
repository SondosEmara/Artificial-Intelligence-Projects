:- consult('students_courses.pl').
%Common Function method in some Tasks.
% Checks to see if first parameter is a member in the list in the second parameter or not
inList(H, [H|_]).
inList(H, [_|T]) :- 
    inList(H, T).

% Takes two lists and appends them
joinLists([], L2, L2).
joinLists([H|T], L2, [H|R]):-
    joinLists(T, L2, R).

%------------------------------------------Problem 1---------------------------------------------------
%The main predidicate that user will call it.
numStudents(CourseName,FinalResult):-
    calculateCount([],CourseName,0,FinalResult).

%Recursion Call.
calculateCount(StoreIds,CourseName,Count,FinalResult):-
         student(ID,CourseName,_),
         not(inList(ID,StoreIds)),
         !,
         NewCount is Count+1,
         joinLists([ID],StoreIds,L),
         calculateCount(L,CourseName,NewCount,FinalResult).
   
%Base Case
calculateCount(_,_,FinalResult,FinalResult).

%-------------------------------------------------------------------------------------------------
%------------------------------------ Problem 2------------------------------------------------------
maxCondition(MG,G,R):-
   MG < G,
   R = G;
   R = MG.

maxStudentGrade(StudentId,MaxGrade):-
       getMaxGrade(StudentId,[],-1,MaxGrade).

getMaxGrade(StudentId,StoreCourse,MGrade,MaxGrade):-
     student(StudentId,X,Grade),
     not(inList(X,StoreCourse)),!,
     maxCondition(MGrade,Grade,NewGrade),
     joinLists([X],StoreCourse,L),
     getMaxGrade(StudentId,L,NewGrade,MaxGrade).
getMaxGrade(_,_,MaxGrade,MaxGrade).
%---------------------------------------------------------------------------------------------------


%----------------------------------------Problem 3---------------------------------------------------


%S --Student, X-- TargetCourse,R--Result,G---Grade

checkConditions(S,X,R,Courses):-

   %Case 1 if student pass the course will be stop and not include X in final Result.

   student(S,X,G),
   (G >= 50),
   remainingAlgorithm(S,X,R,Courses,1),!;

   %Case 2 take the course but not pass it.
   %Case 3 No take any course that will reach to the targetCourse.
   (student(S,X,_);not(prerequisite(_,X))),
   remainingAlgorithm(S,X,false,Courses,2),!;

   %Case 4 stell search for prerequisite courses.
   joinLists([X],R,L),
   remainingAlgorithm(S,X,L,Courses,3),!.
  

remainingCourses(Student,TargetCourse,Courses):-
    remainingAlgorithm(Student,TargetCourse,[],Courses,3).


remainingAlgorithm(Student,Course,Result,Courses,Flag):-
    Flag=:=3,
    prerequisite(X,Course), 
    checkConditions(Student,X,Result,Courses).
    
remainingAlgorithm(_,_,C,C,X):-!.
       
%---------------------------------------------------------------------------------------------



