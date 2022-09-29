from collections import defaultdict

N, M = map(int, input().split())
mod = 10**9+7
# print(mod)
dict = defaultdict(int)
for _ in range(M):
  a = int(input())
  dict[a] += 1

# cnt[i]: i+1段目にたどり着くような場合のかず
cnt = [0] * N
if dict[1] == 0:
  cnt[0] = 1
for i in range(1, N):
  if i == 1:
    if dict[i+1] == 0:
      cnt[i] = cnt[0]+1
  else:
    if dict[i+1] == 0:
      cnt[i] = cnt[i-1]+cnt[i-2]
      cnt[i] %= mod

print(cnt[-1])