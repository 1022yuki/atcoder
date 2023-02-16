import heapq

N, M = map(int, input().split())

edges = []
for i in range(N):
  edges.append([])
for i in range(M):
  a, b, c = map(int, input().split())
  a -= 1
  b -= 1
  edges[a].append((b, c))
  edges[b].append((a, c))

Q = []
heapq.heappush(Q, (0, 0))
dist = [-1]*N
dist[0] = 0
done = [False]*N

while len(Q)>0:
  d, i = heapq.heappop(Q)
  if done[i]:
    continue
  done[i] = True
  for j, c in edges[i]:
    if dist[j]==-1 or dist[j]>dist[i]+c:
      dist[j] = dist[i]+c
      heapq.heappush(Q, (dist[j], j))

# print(dist)

now = N-1
d_sum = dist[N-1]
ans = []
while now != 0:
  ans.append(now)
  for j, c in edges[now]:
    if dist[j] == d_sum-c:
      now = j
      d_sum -= c
      break
ans.append(0)
# print(ans)
ans.reverse()
for i in range(len(ans)):
  ans[i]+=1
print(*ans)