import sys
sys.setrecursionlimit(10**7)

N = int(input())
A = list(map(int, input().split()))

graph = []
for i in range(N):
  graph.append([])
for i in range(N-1):
  graph[A[i]-1].append(i+1)

print(graph)

done = [False]*N
buka = [0]*N
def dfs(i):
  if done[i]:
    return buka[i]
  else:
    sum = 0
    for x in graph[i]:
      sum += dfs(x)+1
    buka[i] = sum
    done[i] = True
    return buka[i]

dfs(2)
print(buka)