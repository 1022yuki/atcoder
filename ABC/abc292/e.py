import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline()[:-1]

N, M = map(int, input().split())

edges = []
edges_rev = []
for i in range(N):
  edges.append([])
  edges_rev.append([])

U = []
V = []
for i in range(M):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  U.append(u)
  V.append(v)
  edges[u].append(v)
  edges_rev[v].append(u)


cnt = 0
def ap_ed(s, e):
  global cnt
  if s==e:
    return
  if not e in edges[s]:
    cnt += 1
    edges[s].append(e)
    edges_rev[e].append(s)
  for ne1 in edges[e]:
    if not ne1 in edges[s]:
      ap_ed(s, ne1)
  for ne2 in edges_rev[s]:
    if not e in edges[ne2]:
      ap_ed(ne2, e)

for i in range(M):
  u = U[i]
  v = V[i]
  ap_ed(u, v)

print(cnt)