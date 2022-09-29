N = int(input())

A = list(map(int, input().split()))

for i in range(0, N):
  sum = A[i]
  for j in range(i+1, N):
    sum += A[j]
  
  if sum < 4:
    N -= 1

print(N)