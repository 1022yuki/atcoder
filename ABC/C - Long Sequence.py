N = int(input())
A = list(map(int, input().split()))
X = int(input())

Asum = 0
for i in range(0, N):
  Asum += A[i]

# B = []
# for _ in range(0, 10**8):
#   B += A

# print(B)

# for i in range(0, 10**100):
#   sum += A[i%len(A)]
#   if sum > X:
#     print(i+1)
#     break

T = X // Asum 

# print(T)

sum = T*Asum

for i in range(0, N):
  sum += A[i]
  if sum > X:
    print(N*T+i+1)
    break