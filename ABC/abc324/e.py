N, T = map(str, input().split())
N = int(N)

S = []
for i in range(N):
  s = input()
  S.append(s)

pre = []
suf = []

for i in range(N):
  k = 0
  s = S[i]
  for j in range(len(S[i])):
    if s[j]==T[k]:
      k += 1
      if k==len(T):
        break
  pre.append(k)
  l = 0
  for j in range(len(S[i])-1, -1, -1):
    if s[j]==T[len(T)-1-l]:
      l += 1
      if l==len(T):
        break
  suf.append(l)

pre.sort()
suf.sort()

ans = 0
import bisect
for i in range(N):
  ind = bisect.bisect_left(suf, len(T)-pre[i])
  ans += N-ind

print(ans)