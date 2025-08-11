parent(john, mary).
parent(john, tom).
parent(mary, alice).

grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
