import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())

edges = []
indeg = [0]*N
for i in range(N):
  edges.append(set())
for i in range(M):
  x, y = map(int, input().split())
  x -= 1
  y -= 1
  edges[y].add(x)
  indeg[x]+=1

for i in range(N):
  edges[i] = list(edges[i])

length = [1]*N
done = [False]*N

def rec(i):
  if done[i]:
    return length[i]
  length[i] = 1
  for j in edges[i]:
    length[i] = max(length[i], rec(j)+1)
  done[i] = True
  return length[i]

# print(indeg)

cnt = 0
for i in range(N):
  if indeg[i] == 0:
    cnt+=1
    if cnt>=2:
      print("No")
      exit()
    rec(i)
    if length[i] != N:
      print("No")
      exit()
    print("Yes")
    print(*length)