N, M = map(int, input().split())
S = list(input())
T = list(input())

from collections import deque

queue = deque()
done = [False]*(N-M+1)

for i in range(N-M+1):
  flag = True
  for j in range(M):
    if S[i+j]!=T[j]:
      flag = False
      break
  if flag:
    queue.append(i)

# print(queue)

while len(queue)>0:
  i = queue.popleft()
  if done[i]:
    continue
  flag = True
  for j in range(M):
    if S[i+j]!=T[j] and S[i+j]!="#":
      flag = False
      break
  if flag:
    for j in range(M):
      S[i+j] = "#"
    done[i] = True
    for dif in range(-M+1, M):
      if i+dif>=0 and i+dif<=N-M:
        queue.append(i+dif)

if set(S)==set(["#"]):
  print("Yes")
else:
  print("No")