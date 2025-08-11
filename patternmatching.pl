pattern_match([], []).
pattern_match([H|T1], [H|T2]) :- pattern_match(T1, T2).
