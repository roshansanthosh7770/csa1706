% state(monkey_position, box_position, monkey_has_banana)
move(state(middle, middle, has_banana), grab, state(middle, middle, has_banana)).
move(state(X, Y, no_banana), walk(X, Z), state(Z, Y, no_banana)).
move(state(P, P, no_banana), climb, state(P, P, no_banana)).
move(state(P, P, no_banana), push(P, Z), state(Z, Z, no_banana)).
move(state(middle, middle, no_banana), grab, state(middle, middle, has_banana)).

goal(state(_, _, has_banana)).
