N, Q = map(int, input().split())

queries = []
for i in range(Q):
  q = list(map(int, input().split()))
  queries.append(q)

li = [0]
for i in range(1, N+1):
  li.append(i)

rev = 1

for i in range(Q):
  query =  queries[i]
  if query[0]==1:
    x, y = query[1], query[2]
    if rev==1:
      li[x] = y
    else:
      li[N-x+1] = y

  if query[0]==2:
    # li.reverse()
    rev *= -1

  if query[0]==3:
    x = query[1]
    # print(li)
    if rev==1:
      print(li[x])
    else:
      print(li[N-x+1])