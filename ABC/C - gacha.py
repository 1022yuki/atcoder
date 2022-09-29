N = int(input())

S = []

for _ in range(0, N):
  s = input()
  S.append(s)

setedS = set(S)

print(len(setedS))