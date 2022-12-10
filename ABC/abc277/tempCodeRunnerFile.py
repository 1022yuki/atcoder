from collections import defaultdict

N = int(input())

# 隣接グラフ(連想配列)
dict = defaultdict(list)

for i in range(N):
  a, b = map(int, input().split())
  dict[a].append(b)
  dict[b].append(a)

print(dict)