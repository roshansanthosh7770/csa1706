:- dynamic(edge/3).

% edge(Node1, Node2, HeuristicCost)
edge(a, b, 4).
edge(a, c, 2).
edge(b, d, 5).
edge(c, d, 1).

best_first_search(Start, Goal, Path) :-
    bfs([[Start]], Goal, Path).

bfs([[Goal|Rest]|_], Goal, [Goal|Rest]).
bfs([Path|Paths], Goal, FinalPath) :-
    Path = [Node|_],
    findall([Next,Node|Path],
            (edge(Node, Next, _), \+ member(Next, Path)),
            NewPaths),
    append(Paths, NewPaths, UpdatedPaths),
    sort_paths(UpdatedPaths, SortedPaths),
    bfs(SortedPaths, Goal, FinalPath).

sort_paths(Paths, Sorted) :-
    map_list_to_pairs(path_cost, Paths, Pairs),
    keysort(Pairs, SortedPairs),
    pairs_values(SortedPairs, Sorted).

path_cost([Node|_], Cost) :-
    edge(Node, _, Cost), !.
path_cost(_, 999).
