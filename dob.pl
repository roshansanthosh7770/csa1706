dob(john, '12-05-1998').
dob(mary, '23-09-2000').
dob(sam, '14-11-1995').

get_dob(Name, DOB) :- dob(Name, DOB).
