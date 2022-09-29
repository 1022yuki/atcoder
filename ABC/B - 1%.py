import math

X = int(input())

money = 100

year = 0

while money < X:
  money += math.floor(money//100)
  year += 1

print(year)