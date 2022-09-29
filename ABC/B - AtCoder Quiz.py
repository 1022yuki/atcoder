S = []

for _ in range(0, 3):
  s = input()
  S.append(s)

S.sort()

# print(S)

if S[0][1] == 'G':
  print('ABC')
elif S[1][1] == 'H':
  print('AGC')
elif S[2][1] == 'R':
  print('AHC')
else:
  print('ARC')