H, W = map(int, input().split())

grid = []
for i in range(H):
  inp = list(map(int, input().split()))
  grid.append(inp)

from collections import defaultdict
import itertools

a = list(range(H+W-2))
comb = list(itertools.combinations(a,H-1))
# print(a)
# print(comb)
lg = len(comb)

ans = 0

for i in range(lg):
  root = comb[i]
  down = [False]*(H+W-2)
  for i in range(H-1):
    down[root[i]] = True
  # print(down)
  dic = defaultdict(int)
  i = 0
  j = 0
  for n in range(H+W-2):
    if dic[grid[i][j]] == 1:
      continue
    dic[grid[i][j]] += 1
    if down[n]:
      i+=1
    else:
      j+=1
  if i == H-1 and j == W-1:
    if dic[grid[i][j]] == 0:
      ans += 1

print(ans)