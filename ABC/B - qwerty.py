P = list(map(int, input().split()))

ANS = []

for i in range(0, 26):
  ANS.append(chr(96+P[i]))

for i in range(0, 26):
  print(ANS[i], end='')

print()