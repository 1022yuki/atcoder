S = input()

from collections import deque
que = deque()

for i in range(len(S)):
  # print(que)
  flagB = False
  if S[i]=='C':
    if len(que)>0 and que[-1]=='B':
      que.pop()
      flagB = True
      if len(que)>0 and que[-1]=='A':
        que.pop()
      else:
        que.append('B')
        que.append('C')
    if not flagB:
      que.append('C')    
  else:
    que.append(S[i])

print(''.join(que))