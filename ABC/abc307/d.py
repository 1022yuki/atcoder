N = int(input())
S = list(input())

from collections import deque
Q = deque()

cnt = 0
for i in range(N):
  Q.append(S[i])
  if S[i]=='(':
    cnt += 1
  if S[i]==')':
    if cnt>0:
      while True:
        po = Q.pop()
        if po=='(':
          cnt -= 1
          break

for i in range(len(Q)):
  print(Q[i], end='')
print()

