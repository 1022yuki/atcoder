N, P = map(int, input().split())

A = list(map(int, input().split()))

count = 0

for i in range(0, N):
  if A[i] < P:
    count += 1

print(count)