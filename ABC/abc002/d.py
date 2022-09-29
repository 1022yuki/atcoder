N, M = map(int, input().split())

relation = []
for m in range(M):
  x, y = map(int, input().split())
  relation.append((x, y))

all = 1<<N
ans = 0

def has_bit(n, i):
  return n & 1<<i > 0 

for n in range(all):
  giin_num = []
  for i in range(N):
    if has_bit(n, i):
      giin_num.append(i+1)
  # print(giin_num)

  ok = True
  for i in range(len(giin_num)):
    for j in range(i+1, len(giin_num)):
      state = False
      p1 = giin_num[i]
      p2 = giin_num[j]
      for x, y in relation:
        if p1 == x and p2 == y:
          state = True
          break
      if not state:
        ok = False
  
  if ok:
    ans = max(ans, len(giin_num))

print(ans)