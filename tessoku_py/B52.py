from collections import deque

N, X = map(int, input().split())
A = [None]+list(input())

# print(A)

queue = deque()
queue.append(X)

A[X] = "@"

# print(A)

while len(queue)>0:
  ind = queue.popleft()
  if ind-1>=1 and A[ind-1] == ".":
    A[ind-1] = "@"
    queue.append(ind-1)
  if ind+1<=N and A[ind+1] == ".":
    A[ind+1] = "@"
    queue.append(ind+1)

print("".join(A[1:]))