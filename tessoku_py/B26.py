N = int(input())

dlt = [False] * (N+1)
lim1 = int(N**0.5)
for i in range(2, lim1+1):
  if dlt[i]:
    continue
  lim2 = N // i
  for j in range(2, lim2+1):
    dlt[i*j] = True

for i in range(2, N+1):
  if not dlt[i]:
    print(i)