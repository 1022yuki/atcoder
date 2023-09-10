# 再帰で解く
import sys
sys.setrecursionlimit(10**7)
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=0') 

N = int(input())

# 隣接リスト
edges = []
for i in range(N+1):
  edges.append([0]*(N+1))

for i in range(N-1):
  D = list(map(int, input().split()))
  for j in range(len(D)):
    edges[i][i+j+1] = D[j]
    edges[i+j+1][i] = D[j]

if N%2==1:
  N+=1

ans = -1
used = [False]*N
def rec(w):
  global ans
  ans = max(ans, w)
  i = 0
  while i<N and used[i]:
    i += 1
  if i==N:
    return 0
  used[i] = True
  # rec(w)
  for j in range(i+1, N):
    if used[j]:
      continue
    used[j] = True
    rec(w+edges[i][j])
    used[j] = False
  used[i] = False

rec(0)

print(ans)