import sys
def input(): return sys.stdin.readline()[:-1]
from collections import defaultdict

N = int(input())
S = []
for i in range(N):
  s = input()
  S.append(s)

ss = sorted(S)

dic = defaultdict(int)

def check(s, t):
  rg = min(len(s), len(t))
  ret = 0
  for i in range(rg):
    if s[i] == t[i]:
      ret += 1
    else:
      break
  return ret

for i in range(N):
  if i!=0:
    s1 = ss[i-1]
    s2 = ss[i]
    cond1 = check(s1, s2)
    dic[ss[i]] = max(dic[ss[i]], cond1)
  
  if i!=N-1:
    s1 = ss[i+1]
    s2 = ss[i]
    cond2 = check(s1, s2)
  
  dic[ss[i]] = max(dic[ss[i]], cond2)

for i in range(N):
  print(dic[S[i]])