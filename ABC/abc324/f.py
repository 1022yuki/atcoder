import sys
def input(): return sys.stdin.readline()[:-1]
INF = 10**7

N, M = map(int, input().split())

edges = []
for i in range(N):
  edges.append([])

for i in range(M):
  u, v, b, c = map(int, input().split())
  u -= 1
  v -= 1
  edges[u].append([v, b, c])
  edges[v].append([u, b, c])

ng = 10**4
ok = 0

# ダイクストラ法は負の辺があると使えない
# def check(x):
#   dist = [INF*(-1)]*N
#   dist[0] = 0
#   Q = []
#   heapq.heappush(Q, (0, 0))
#   done = [False]*N
#   while len(Q)>0:
#     d, i = heapq.heappop(Q)
#     if done[i]:
#       continue
#     done[i] = True
#     for j, b, c in edges[i]:
#       if dist[j]==INF*(-1) or dist[i]+((x*c)-b) < dist[j]:
#         dist[j] = dist[i]+((x*c)-b)
#         heapq.heappush(Q, (dist[j], j))
#   if dist[N-1]<=0:
#     return True
#   else:
#     return False

def check(x):
  dist = [INF]*N
  dist[0] = 0
  for i in range(N-1):
    for j, b, c in edges[i]:
      if dist[j]==INF or dist[i]+((x*c)-b) < dist[j]:
        dist[j] = dist[i]+((x*c)-b)
  if dist[N-1]<=0:
    return True
  else:
    return False

while abs(ok-ng)>10**(-9):
  mid = (ok+ng)/2
  if check(mid):
    ok = mid
  else:
    ng = mid

print(ok)