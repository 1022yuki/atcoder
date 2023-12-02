N = int(input())

S = []
for i in range(N):
  s = input()
  S.append(s)

Rcount = []
Ccount = []
for i in range(N):
  cnt = 0
  for j in range(N):
    if S[i][j] == "o":
      cnt += 1
  Rcount.append(cnt)

for j in range(N):
  cnt = 0
  for i in range(N):
    if S[i][j] == "o":
      cnt += 1
  Ccount.append(cnt)

ans = 0
for i in range(N):
  for j in range(N):
    if S[i][j] == "o":
      ans += (Rcount[i]-1)*(Ccount[j]-1)

print(ans)