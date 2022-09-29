N, M = map(int, input().split())

A = []

for i in range(N):
  A.append(list(map(int, input().split())))

# print(A)

ans = 0

for i in range(M):
  for j in range(i+1, M):
    # print(str(i) + str(j))

    point = 0

    for player in range(N):
      p = max(A[player][i], A[player][j])
      point += p
    
    ans = max(ans, point)

print(ans)