# формула:
# сума = депозирана сума + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

depositedSum = float(input())

depositDue = int(input())

yearlyInterestPercent = float(input())
interest = depositedSum * (yearlyInterestPercent / 100)
monthlyInterest = interest / 12
result = depositedSum + (depositDue * monthlyInterest)

print(result)