N, L = map(int, input().split())

P = []
for i in range(N):
  a, b = map(str, input().split())
  P.append([int(a), b])

ans = -1

for i in range(N):
  a, b = P[i]
  if b == "E":
    cond = L-a
  if b == "W":
    cond = a
  ans = max(ans, cond)

print(ans)