diet(diabetes, 'Low sugar, high fiber foods').
diet(hypertension, 'Low salt, more vegetables').
diet(obesity, 'Low carb, high protein').

suggest_diet(Disease, Diet) :- diet(Disease, Diet).
