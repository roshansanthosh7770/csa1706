fact(a).
fact(b).
rule(c) :- fact(a), fact(b).

ask(Goal) :-
    fact(Goal);
    rule(Goal).
