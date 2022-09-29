from collections import defaultdict

N, K = map(int, input().split())
S = []
for i in range(N):
  S.append(input())

def has_bit(n, i):
  return n & 1<<i > 0

ans = 0

for n in range(1<<N):
  dict = defaultdict(int)
  for i in range(N):
    if has_bit(n, i):
      st = S[i]
      for x in st:
        dict[x] += 1
  cnt = 0
  for value in dict.values():
    if value == K:
      cnt += 1
  ans = max(ans, cnt)

print(ans)