symptom(fever, flu).
symptom(cough, flu).
symptom(rash, measles).

diagnose(Symptoms, Disease) :-
    symptom(Symptom, Disease),
    member(Symptom, Symptoms).
