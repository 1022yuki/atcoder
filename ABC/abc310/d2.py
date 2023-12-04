import math
import sys
# def input(): return sys.stdin.readline()[:-1]
sys.setrecursionlimit(10**7)
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=0') 

N, T, M = map(int, input().split())

Bad = []
for i in range(N):
  Bad.append(set())
for i in range(M):
  a, b = map(int, input().split())
  a-=1
  b-=1
  Bad[a].add(b)
  Bad[b].add(a)

cnt = 0
def dfs(i: int, team: list, has_member_team: int):
  # print(i, team)
  global cnt
  if i==N:
    if has_member_team==T:
      cnt += 1
    return
  for t in range(T):
    if len(team[t])==0:
      team[t].add(i)
      dfs(i+1, team, has_member_team+1)
      team[t].remove(i)
      break
    else:
      if team[t].isdisjoint(Bad[i]):
        team[t].add(i)
        dfs(i+1, team, has_member_team)
        team[t].remove(i)

team = []
for i in range(T):
  team.append(set())
dfs(0, team, 0)
print(cnt)