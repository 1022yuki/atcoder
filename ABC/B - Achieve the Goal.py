N, K, M = map(int, input().split())
A = list(map(int, input().split()))

sum = 0
for i in A:
  sum += i

if N*M-sum > K:
  print(-1)
elif N*M-sum < 0:
  print(0)
else:
  print(N*M-sum) 