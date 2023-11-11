import sys
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())

edges = []
for i in range(N):
  edges.append([])
indeg = [0] * N

for _ in range(M):
  x, y = map(int, input().split())
  edges[x-1].append(y-1)
  indeg[y-1] += 1

# print(edges)
# print(indeg)

done = [False] * N

length = [0] * N
def rec(i):
  if done[i]:
    return length[i]
  else:
    for j in edges[i]:
      length[i] = max(length[i], rec(j)+1)
    done[i] = True
    return length[i]

ans_li = []
for i in range(N):
  if indeg[i] == 0:
    ans_li.append(rec(i))

print(max(ans_li))