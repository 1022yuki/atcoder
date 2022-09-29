from sys import setrecursionlimit
setrecursionlimit(1000000)

N = int(input())

edges = []
for i in range(N):
  edges.append([])

for i in range(N):
  p = int(input())
  if p == -1:
    R = i
  else:
    edges[p-1].append(i)

# aの値ごとqueryをまとめる
queries = []
for i in range(N):
  queries.append([])
Q = int(input())
for q in range(Q):
  a, b = map(int, input().split())
  queries[a-1].append([q, b-1])

# ans[i]: 答えとなる配列
ans = [False] * Q
# boss[i]: 頂点iが今見ている頂点の上司ならTrue
boss = [False] * N

# dfs実装
def dfs(i):
  for q, b in queries[i]:
    ans[q] = boss[b]
  boss[i] =True
  for j in edges[i]:
    dfs(j)
  boss[i] = False

dfs(R)

for q in range(Q):
  if ans[q]:
    print('Yes')
  else:
    print('No')