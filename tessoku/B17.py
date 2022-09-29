N = int(input())
H = list(map(int, input().split()))

dp = [None] * N
dp[0] = 0
dp[1] = abs(H[1]-H[0])

for i in range(2, N):
  dp[i] = min(dp[i-1]+abs(H[i]-H[i-1]), dp[i-2]+abs(H[i]-H[i-2]))

# print(dp)

Place = N-1
ans = []

while True:
  ans.append(Place+1)
  if Place == 0:
    break
  
  if dp[Place] == dp[Place-1] + abs(H[Place]-H[Place-1]):
    Place -= 1
  else:
    Place -= 2

ans.reverse()
# print(ans)

print(len(ans))
print(*ans)