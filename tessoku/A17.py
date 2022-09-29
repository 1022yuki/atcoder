N = int(input())
A = [0]*2 + list(map(int, input().split()))
B = [0]*3 + list(map(int, input().split()))

dp = [None] * (N+1)
dp[1] = 0
dp[2] = A[2]

for i in range(3, N+1):
  dp[i] = min(dp[i-1]+A[i], dp[i-2]+B[i])

# print(dp)

Ans = []
Place = N
while True:
  Ans.append(Place)
  if Place == 1:
    break
  if dp[Place] == dp[Place-1] + A[Place]:
    Place -= 1
  else:
    Place -= 2

# print(Ans)

Ans.reverse()

print(len(Ans))
print(*Ans)