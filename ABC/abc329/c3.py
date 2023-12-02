N = int(input())
S = list(input())

# pres = set(S)
# print(pres)

from collections import defaultdict
dic = defaultdict(int)

rep = 0
for i in range(N):
  # if dic[S[i]] == 0:
  #   dic[S[i]] = 1
  if S[i] == S[i-1]:
    rep += 1
  else:
    rep = 1
  dic[S[i]] = max(dic[S[i]], rep)
  
# print(dic)

ans = 0
for v in dic.values():
  ans += v

print(ans)