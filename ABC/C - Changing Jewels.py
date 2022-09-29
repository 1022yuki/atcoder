N, X, Y = map(int, input().split())

ju = []
for i in range(N):
  ju.append([0, 0])

ju[0][0] += 1

# print(ju)

for i in range(N-1):
  ju[i+1][0] += ju[i][0]
  ju[i][1] += ju[i][0] * X

  ju[i+1][1] += ju[i][1] * Y
  ju[i+1][0] += ju[i][1]

print(ju[N-1][1])