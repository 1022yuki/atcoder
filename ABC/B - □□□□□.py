import math

n = int(input())

# print(int(math.sqrt(n)))

SUM = []

for i in range(0, int(math.sqrt(n))):
  sq = n // (i+1) - (i+1)
  rem = n % (i+1)

  sum = sq + rem

  # print(sum)

  SUM.append(sum)

print(min(SUM))