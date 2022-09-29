import heapq

n, k = map(int, input().split())

E = []
for i in range(n):
  E.append([])

for _ in range(k):

  inp = list(map(int, input().split()))

  if inp[0] == 0:
    a, b = inp[1:]
    a -= 1
    b -= 1
    
    dist = [-1] * n
    dist[a] = 0

    done = [False] * n

    Q = []
    heapq.heappush(Q, (0, a))

    while(len(Q)>0):

      d, i = heapq.heappop(Q)

      if done[b]:
        break

      if done[i]:
        continue
      
      done[i] = True
      for d2, j in E[i]:
        if dist[j] == -1 or dist[j] > d + d2:
          dist[j] = d + d2
          heapq.heappush(Q, (dist[j], j))
    
    print(dist[b])


  if inp[0] == 1:
    c, d, e = inp[1:]
    c -= 1
    d -= 1
    E[c].append((e, d))
    E[d].append((e, c))