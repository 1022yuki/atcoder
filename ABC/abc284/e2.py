import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline()[:-1]
import pypyjit
pypyjit.set_param('max_unroll_recursion=0')  
N, M = map(int, input().split())

edges = []
for i in range(N):
  edges.append([])

for i in range(M):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  edges[a].append(b)
  edges[b].append(a)

# print(edges)
visited = [False]*N
visited[0] = True

cnt = 0
def dfs(i):
  global cnt
  if cnt == 10**6:
    print(cnt)
    exit()
  cnt+=1
  for j in edges[i]:
    if not visited[j]:
      visited[j]=True
      dfs(j)
      visited[j]=False

dfs(0)
print(cnt)