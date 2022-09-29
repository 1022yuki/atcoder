from collections import defaultdict, deque

Q = int(input())

que = deque()

for _ in range(Q):
  query = list(input().split())
  # print(query)
  if query[0] == '1':
    c = query[1]
    x = int(query[2])
    que.append([c, x])
    # print(que)

  if query[0] == '2':
    d = int(query[1])
    dict = defaultdict(int)
    sum = 0
    while sum < d and len(que) > 0:
      c, x = que[0]
      sum += x
      if sum <= d:
        c, x = que.popleft()
        dict[c] += x
      else:
        que[0][1] = sum-d
        dict[c] += x-sum+d
    # print(dict)
    # print(que)

    ans = 0
    for value in dict.values():
      ans += value**2
    
    print(ans)