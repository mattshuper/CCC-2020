# There are three lines of input. Each line contains one positive integer. The first line contains the
# value of P. The second line contains N, the number of people who have the disease on Day 0. The
# third line contains the value of R. Assume that P ≤ 107
# and N ≤ P and R ≤ 10.

infected = 0
days = 0

sickLimit = int(input())
dayZeroInfected = int(input())
infectingAbility = int(input())

infected += dayZeroInfected
canInfect = dayZeroInfected
while infected <= sickLimit:
    infected += canInfect * infectingAbility
    canInfect = canInfect * infectingAbility
    days += 1

print(days)


