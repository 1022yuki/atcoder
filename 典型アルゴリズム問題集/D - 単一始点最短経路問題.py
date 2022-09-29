import heapq

N, M = map(int, input().split())

E = [[] for _ in range(N)]
for i in range(M):
  u, v, c = map(int, input().split())
  E[u].append((v, c))

# print(E)

Q = []
heapq.heappush(Q, (0,0))

time = [-1] * N
time[0] = 0

done = [False] * N 

while(len(Q)>0):
  d, i = heapq.heappop(Q)

  if done[i]:
    continue

  done[i] = True

  for j, t in E[i]:
    if time[j] == -1 or time[j] > time[i]+t:
      time[j] = time[i] + t
      heapq.heappush(Q, (time[j], j))

print(time[-1])