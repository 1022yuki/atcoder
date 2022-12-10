from collections import defaultdict
N, Q = map(int, input().split())

edges = defaultdict(dict)

queries = []
for i in range(Q):
  inp = list(map(int, input().split()))
  queries.append(inp)

for i in range(Q):
  query = queries[i]
  a = query[1]
  b = query[2]

  if query[0] == 1:
    # print(edges[a])
    if b not in edges[a]:
      edges[a][b] = 0
    edges[a][b] += 1
    
    # print(edges)
  
  if query[0] == 2:
    if b in edges[a]:
      if edges[a][b]>=1:
        edges[a][b] = 0

  if query[0] == 3:
    if b in edges[a] and a in edges[b]:
      if edges[a][b] >= 1 and edges[b][a] >= 1:
        print('Yes')
      else:
        print('No')
    else:
      print('No')

# print(edges)