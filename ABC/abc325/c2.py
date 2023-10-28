import sys
# def input(): return sys.stdin.readline()[:-1]
sys.setrecursionlimit(10**7)
import pypyjit
pypyjit.set_param('max_unroll_recursion=0') 

H, W = map(int, input().split())
S = []
for i in range(H):
  S.append(input())

visited = [-1]*(H*W)

num = 0
def dfs(i, j):
  visited[i*W+j] = num
  for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
    ni = i+di
    nj = j+dj
    if ni<0 or ni>=H or nj<0 or nj>=W:
      continue
    if S[ni][nj]==".":
      continue
    if visited[ni*W+nj]!=-1:
      continue
    dfs(ni, nj)

for i in range(H):
  for j in range(W):
    if S[i][j]==".":
      continue
    if visited[i*W+j]!=-1:
      continue
    dfs(i, j)
    num += 1

print(num)