N, Q = map(int, input().split())

S = list(input())


count = 0
for i in range(0, Q):
  query = list(map(int, input().split()))


  if query[0] == 1:
    
    x = query[1]
  
    count += x


  if query[0] == 2:

    x = query[1]

    print(S[(-count+x-1)%N])