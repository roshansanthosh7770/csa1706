def vacuum_cleaner(location, status_A, status_B):
    actions = []
    if location == "A":
        if status_A == "Dirty":
            actions.append("Suck")
            status_A = "Clean"
        actions.append("Move Right")
        location = "B"
        if status_B == "Dirty":
            actions.append("Suck")
            status_B = "Clean"
    else:
        if status_B == "Dirty":
            actions.append("Suck")
            status_B = "Clean"
        actions.append("Move Left")
        location = "A"
        if status_A == "Dirty":
            actions.append("Suck")
            status_A = "Clean"
    return actions

loc = input("Enter initial location (A/B): ").strip().upper()
a_status = input("Enter status of A (Clean/Dirty): ").strip().capitalize()
b_status = input("Enter status of B (Clean/Dirty): ").strip().capitalize()

result = vacuum_cleaner(loc, a_status, b_status)

for step in result:
    print(step)
