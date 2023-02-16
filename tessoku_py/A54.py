from collections import defaultdict

Q = int(input())

queries = []
for i in range(Q):
  inp = input().split()
  queries.append(inp)

dict = defaultdict(int)

for i in range(Q):
  query = queries[i]
  if query[0] == '1':
    dict[query[1]] = query[2]
  if query[0] == '2':
    print(dict[query[1]])