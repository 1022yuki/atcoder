N, K = map(int, input().split())

P = list(map(int, input().split()))

P.sort()

sum = 0

for i in range(0, K):
  sum += P[i]

print(sum)