N, M = map(int, input().split())

edges = []
for i in range(N+1):
  edges.append([])
for i in range(M):
  a, b = map(int, input().split())
  edges[a].append(b)
  edges[b].append(a)

# print(edges)

for i in range(1, N+1):
  print(str(i)+": {", end="")

  ans_li = edges[i]
  for j in range(len(ans_li)):
    print(ans_li[j], end="")
    if j != len(ans_li)-1:
      print(", ", end="")
  
  print("}")