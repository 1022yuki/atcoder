import sys
# def input(): return sys.stdin.readline()[:-1]
sys.setrecursionlimit(10**7)
import pypyjit
pypyjit.set_param('max_unroll_recursion=0') 

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

edges = []
for i in range(N):
  edges.append([])

for i in range(M):
  if A[i]==B[i]:
    print('No')
    exit()
  # A[i]とB[i]を無向辺で結んだ時に奇数長の閉路ができるかどうかを判定する
  edges[A[i]-1].append(B[i]-1)
  edges[B[i]-1].append(A[i]-1)

colors = [-1]*N

# グラフが二部グラフかどうか判定
# dfs
def dfs(i, color):
  colors[i] = color
  for j in edges[i]:
    if colors[j]==color:
      return False
    if colors[j]==-1 and not dfs(j, 1-color):
      return False
  return True

flag = True
for i in range(N):
  if colors[i]==-1:
    if not dfs(i, 0):
      flag = False

if flag:
  print('Yes')
else:
  print('No')