n = int(input())

N = 10**6
# O(loglogn)
dlt = [False] * (N+1)
lim1 = int(N**0.5)
for i in range(2, lim1+1):
  if dlt[i]:
    continue
  lim2 = N // i
  for j in range(2, lim2+1):
    dlt[i*j] = True

li = []
for i in range(2, N+1):
  if not dlt[i]:
    li.append(i)

lg = len(li)
ans = 0
for i in range(lg):
  for j in range(i+1, lg):
    p = li[i]
    q = li[j]
    if p*q*q*q > n:
      break
    ans += 1

print(ans)