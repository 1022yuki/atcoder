import heapq

N, M = map(int, input().split())

E = [[] for _ in range(N)]
for i in range(M):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  E[a].append(b)
  E[b].append(a)

Q = []
heapq.heappush(Q, (0, 0))

dist = [-1] * N
dist[0] = 0

done = [False] * N

x = 1

while(len(Q)>0):

  d, i = heapq.heappop(Q)

  if done[i]:
    continue
  
  done[i] = True

  for j in E[i]:
    # 未訪問またはiからjまでの距離がその時点でのjへの最短距離よりも小さいとき
    if dist[j] == -1 or d + x < dist[j]:
      dist[j] = d + x
      heapq.heappush(Q, (dist[j], j))

# print(Q)
# print(dist)

if dist[-1] == 2:
  print('POSSIBLE')
else:
  print('IMPOSSIBLE')