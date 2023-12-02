N = int(input())
S = input()

# print(S.count(">"))

from collections import defaultdict
dic = defaultdict(int)

rep = 0
for i in range(N-1):
  if S[i]==">":
    rep += 1
    if i==N-2:
      dic[rep] += 1
  else:
    dic[rep] += 1
    rep = 0

# print(dic)

ans = 0
for k, v in dic.items():
  ans += (k*(k+1)//2)*v

print(ans)