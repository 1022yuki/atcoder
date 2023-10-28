import sys
def input(): return sys.stdin.readline()[:-1]
from collections import deque
import heapq

N = int(input())

TimeInAndTimeOut = []
for i in range(N):
  t, d = map(int, input().split())
  TimeInAndTimeOut.append([t, t+d])

TimeInAndTimeOut.sort()

dq1 = deque()
for i in range(N):
  dq1.append(TimeInAndTimeOut[i])

Q = []
cnt = 0
nowTime = 0
lastStampTime = 0
while True:
  # print(nowTime, lastStampTime, dq1, Q)
  if len(dq1)==0 and len(Q)==0:
    break
  while True:
    if len(dq1)==0:
      break
    if dq1[0][0] <= nowTime:
      inTime, outTime = dq1.popleft()
      heapq.heappush(Q, outTime)
    else:
      break
  while len(Q) > 0:
    ot = heapq.heappop(Q)
    if ot>=nowTime and nowTime>=lastStampTime+1:
      cnt += 1
      lastStampTime = nowTime
      break
  if len(Q)==0 and len(dq1)>0:
     nowTime = dq1[0][0]
  else:
    nowTime += 1

print(cnt)