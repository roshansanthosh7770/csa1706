vowel(a). vowel(e). vowel(i). vowel(o). vowel(u).

count_vowels([], 0).
count_vowels([H|T], Count) :-
    count_vowels(T, Rest),
    (vowel(H) -> Count is Rest + 1 ; Count = Rest).
