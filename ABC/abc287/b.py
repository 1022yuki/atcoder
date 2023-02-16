N, M = map(int, input().split())
S = []
T = []
for i in range(N):
  s = list(input())
  S.append(s[-3:])
for i in range(M):
  t = list(input())
  T.append(t)

ans = 0
for i in range(N):
  sn = S[i]
  # print(sn)
  for j in range(M):
    if T[j] == sn:
      ans += 1
      break

print(ans)