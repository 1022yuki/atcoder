N, M = map(int, input().split())

edges = []
for i in range(N+1):
  edges.append([])
for i in range(M):
  a, b = map(int, input().split())
  edges[a].append(b)
  edges[b].append(a)

for i in range(1, N+1):
  ans_li = edges[i]
  ans_li.sort()
  num = len(ans_li)
  ans_li = [num]+ans_li
  print(*ans_li)