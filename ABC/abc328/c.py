N, Q = map(int, input().split())
S = input()

Qs = []
for i in range(Q):
  l, r = map(int, input().split())
  l -= 1
  r -= 1
  Qs.append([l, r])

Sames = []
for i in range(len(S)-1):
  if S[i]==S[i+1]:
    Sames.append(i)

# print(Sames)

import bisect

for i in range(Q):
  l, r = Qs[i]
  l = bisect.bisect_left(Sames, l)
  r = bisect.bisect_left(Sames, r)
  print(r-l)
