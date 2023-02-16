from collections import deque
Q = int(input())

queries = []
for i in range(Q):
  queries.append(input().split())

# print(queries)

stuck = deque()

for i in range(Q):
  query = queries[i]
  if query[0] == '1':
    stuck.append(query[1])
  if query[0] == '2':
    # op = stuck.pop()
    # print(op)
    # stuck.append(op)
    print(stuck[-1])
  if query[0] == '3':
    stuck.pop()