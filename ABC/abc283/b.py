N = int(input())
A = list(map(int, input().split()))
Q = int(input())
que = []
for i in range(Q):
  que.append(list(map(int, input().split())))

# print(que)

for i in range(Q):
  query = que[i]
  # print(query)
  if query[0] == 1:
    k, x = query[1], query[2]
    A[k-1] = x
  if query[0] == 2:
    k = query[1]
    print(A[k-1])