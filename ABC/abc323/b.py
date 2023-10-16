N = int(input())

S = []
for i in range(N):
  s = input()
  S.append(s)

NumWin = [0] * N

for i in range(N):
  for j in range(N):
    if S[i][j] == 'o':
      NumWin[i] += 1

# print(NumWin)

WhoWin = []
for i in range(N):
  WhoWin.append([NumWin[i], (i+1)*(-1)])

WhoWin.sort(reverse=True)
# print(WhoWin)

ans = []
for i in range(N):
  ans.append(WhoWin[i][1]*(-1))

print(*ans)