import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
S = []
for i in range(N):
  s = input()
  S.append(s)
T = set()
for i in range(M):
  t = input()
  T.add(t)

max_un = 16-(N-1)
for i in range(N):
  max_un -= len(S[i])
used = [False]*N

def dfs(i: int, s: str, un: int):
  if i==N:
    if len(s)<3:
      return False
    if len(s)>16:
      return False
    if s in T:
      return False
    print(s)
    exit()
  if un:
    dfs(i, s+'_', un-1)
  for j in range(N):
    if not used[j]:
      used[j] = True
      dfs(i+1, s+'_'+S[j], un)
      used[j] = False
  return False

for i in range(N):
  used[i] = True
  dfs(1, S[i], max_un)
  used[i] = False

print(-1)