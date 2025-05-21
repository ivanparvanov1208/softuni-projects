pagesInABook = int(input())

pagesPerHour = int(input())

daysDue = int(input())

timeForReading = pagesInABook // pagesPerHour

requiredHoursPerDay = timeForReading / daysDue

print(requiredHoursPerDay)