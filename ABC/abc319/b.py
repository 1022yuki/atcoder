N = int(input())

ans = ''

for i in range(N+1):
  si = 100
  for j in range(1, 10):
    if i % (N/j) == 0:
      si = min(si, j)
  if si != 100:
    ans+=str(si)
  else:
    ans+='-'

print(ans)