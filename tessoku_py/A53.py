import heapq
Q = int(input())

queries = []
for i in range(Q):
  queries.append(input().split())
# print(queries)

hp = []

for i in range(Q):
  query = queries[i]
  if query[0] == '1':
    heapq.heappush(hp, int(query[1]))
    # print(hp)
  if query[0] == '2':
    print(hp[0])
  if query[0] == '3':
    heapq.heappop(hp)