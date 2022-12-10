N = int(input())
H = [0]+list(map(int, input().split()))

dp = [None] * (N+1)
dp[1] = 0
dp[2] = abs(H[2]-H[1])

for i in range(3, N+1):
  dp[i] = min(dp[i-1]+abs(H[i]-H[i-1]), dp[i-2]+abs(H[i]-H[i-2]))

# print(dp)
ans = []

place = N
while True:
  ans.append(place)
  if place == 1:
    break
  if dp[place] == dp[place-1] + abs(H[place]-H[place-1]):
    place -= 1
  else:
    place -= 2

ans.reverse()

print(len(ans))
print(*ans)