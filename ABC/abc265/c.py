from collections import deque

H, W = map(int, input().split())

G = []
for i in range(H):
  G.append(list(input()))

# print(G)

Q = deque()
Q.append([0, 0])

visited = []
for i in range(H):
  visited.append([False] * W)

# visited[0][0] = True

# print(visited)

while len(Q)>0:
  i, j = Q.popleft()
  visited[i][j] = True

  if G[i][j] == 'U':
    if i != 0:
      if not visited[i-1][j]:
        Q.append([i-1, j])
      else:
        print(-1)
        exit()

  if G[i][j] == 'D':
    if i != H-1:
      if not visited[i+1][j]:
        Q.append([i+1, j])
      else:
        print(-1)
        exit()
  
  if G[i][j] == 'L':
    if j != 0:
      if not visited[i][j-1]:
        Q.append([i, j-1])
      else:
        print(-1)
        exit()

  if G[i][j] == 'R':
    if j != W-1:
      if not visited[i][j+1]:
        Q.append([i, j+1])
      else:
        print(-1)
        exit()

print(i+1, j+1)