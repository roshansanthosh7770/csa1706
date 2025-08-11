fact(a).
rule(a, b).
rule(b, c).

forward_chaining :-
    (rule(X, Y), fact(X), \+ fact(Y), assert(fact(Y)), fail);
    forall(fact(F), writeln(F)).
