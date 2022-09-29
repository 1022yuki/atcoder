H, W = map(int, input().split())

S = []

for i in range(0, H):
  s = input()
  S.append(s)

O = []
for i in range(0, H):
  O.append([False]*W)

I = []
J = []

for i in range(0, H):
  for j in range(0, W):
    if S[i][j] == "o":
      O[i][j] = True
      I.append(i)
      J.append(j)

dis = abs(I[0]-I[1]) + abs(J[0]-J[1])

print(dis)