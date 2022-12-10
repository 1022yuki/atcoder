from collections import deque

Q = int(input())

queries = []
for i in range(Q):
  queries.append(input().split())

# print(queries)

dq = deque()

for i in range(Q):
  query = queries[i]
  if query[0] == '1':
    dq.append(query[1])
  if query[0] == '2':
    print(dq[0])
  if query[0] == '3':
    dq.popleft()
  