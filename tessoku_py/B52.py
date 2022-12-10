from collections import deque

N, X = map(int, input().split())
A = list(input())

que = deque()
que.append(X)
A[X-1] = '@'

print(A)

while len(que)!=0:
  pos = que.popleft()
  if A[pos-2] == '.':
    que.append(pos-1)
    A[pos-2] = '@'
  if A[pos] == '.':
    que.append(pos+1)
    A[pos] = '@'

print(A)