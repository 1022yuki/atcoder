import sys
sys.setrecursionlimit(10**7)

N = int(input())
A = list(map(int, input().split()))

graph = []
for i in range(N):
  graph.append([])
for i in range(N-1):
  buk = i+1
  jousi = A[i]-1
  graph[jousi].append(buk)

done = [False]*N
buka = [0]*N

# iの部下の数を返す
def dfs(i):
  if done[i]:
    return buka[i]
  else:
    sum = 0
    for bu in graph[i]:
      buka_num = dfs(bu)+1
      sum += buka_num
    buka[i] = sum
    done[i] = True
    return buka[i]

for i in range(N):
  print(dfs(i), end=" ")
print()

# done = [False]*N
# buka = [0]*N
# def dfs(i):
#   if done[i]:
#     return buka[i]
#   else:
#     sum = 0
#     for x in graph[i]:
#       sum += dfs(x)+1
#     buka[i] = sum
#     done[i] = True
#     return buka[i]

# dfs(2)
# print(buka)