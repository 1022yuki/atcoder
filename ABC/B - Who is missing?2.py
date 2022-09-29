N = int(input())

count = [0] * N
# print(count)

A = list(map(int, input().split()))

for i in range(0, 4*N-1):
  num = A[i]
  count[num-1] += 1

# print(count)

for i in range(0, N):
  if count[i] == 3:
    print(i+1)