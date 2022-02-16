#There are three lines of input. Each line contains a non-negative integer less than 10. The first line
#contains the number of small treats, S, the second line contains the number of medium treats, M,
#and the third line contains the number of large treats, L, that Barley receives in a day.

happinessScore = 0

smallTreats = int(input())
mediumTreats = int(input())
largeTreats = int(input())

#Score determination

happinessScore += smallTreats * 1
happinessScore += mediumTreats * 2
happinessScore += largeTreats * 3

if happinessScore >= 10:
    print("happy")
else:
    print("sad")

