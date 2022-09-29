N, M = map(int, input().split())

A = list(map(int, input().split()))

sum = 0

for i in A:
  sum += i

if sum > N:
  print(-1)
else:
  print(N-sum)