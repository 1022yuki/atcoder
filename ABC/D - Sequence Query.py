Q = int(input())

A = []

for i in range(0, Q):
  query = list(map(int, input().split()))
  x = query[1]

  if query[0] == 1:
    A.append(query[1])

  if query[0] == 2:
    k = query[2]
    A.sort()
    # Aのx以下の要素を数える変数
    for i in range(0, len(A)):
      if A[i] >= x:
        num = i
        break
    print('&&&&&&&&&')
    print(num)

    num = sum(i<=x for i in A)
    print('&&&&&&&&&')
    print(num)
    if num < k:
      print(-1)
    else:
      # li = A[0:num]
      # ans = li[len(li)-k]
      ans = A[num-k]
      print(ans)
    
  if query[0] == 3:
    k = query[2]
    A.sort()
    A.reverse()
    # Aのx以上の要素を数える変数
    for i in range(0, len(A)):
      if A[i] < x:
        num = i
        break
    print('%%%%%%%%%%')
    print(num)

    num = sum(i>=x for i in A)
    print('%%%%%%%%%')
    print(num)
    if num < k:
      print(-1)
    else:
      # li = A[0:num]
      # ans = li[len(li)-k]
      ans = A[num-k]
      print(ans)