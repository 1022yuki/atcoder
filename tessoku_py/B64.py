import heapq

N, M = map(int, input().split())

edges = []
for i in range(N):
  edges.append([])
for i in range(M):
  a, b, c = map(int, input().split())
  a -= 1
  b -= 1
  edges[a].append([c, b])
  edges[b].append([c, a])

Q = []
heapq.heappush(Q, (0, 0))

dist = [-1]*N
done = [False]*N

dist[0] = 0

while len(Q)>0:
  d, i = heapq.heappop(Q)

  if done[i]:
    continue
  
  done[i] = True

  for c, j in edges[i]:
    if dist[j] == -1 or dist[j]>dist[i]+c:
      dist[j] = dist[i]+c
      heapq.heappush(Q, (dist[j], j))

# print(dist)
# import sys
# sys.setrecursionlimit(10**7)

# ans = []
# # now = N-1

# def rec(now):
#   ans.append(now)
#   if now == 0:
#     # print(ans)
#     ans.reverse()
#     for x in ans:
#       print(x+1, end=" ")
#     print()
#     return
#   for c, j in edges[now]:
#     if dist[now] == dist[j]+c:
#       rec(j)
#       ans.pop()
# rec(N-1)
ans = [N-1]
now = N-1

while now!=0:
  for c, j in edges[now]:
    if dist[j]+c==dist[now]:
      now = j
      ans.append(j)
# print(ans)

ans.reverse()
for i in range(len(ans)):
  print(ans[i]+1, end=" ")
print()