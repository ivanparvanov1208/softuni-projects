while True:
    destination = input()
    if destination != "End":
        minBudget = float(input())
        sumSavings = 0
        while True:
            savingAmount = float(input())
            sumSavings += savingAmount

            if sumSavings >= minBudget:
                print(f"Going to {destination}!")
                break
    elif destination == "End":
        break