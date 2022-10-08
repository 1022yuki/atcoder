N, M = map(int, input().split())

dp = []
for i in range(N):
  dp.append([-1]*9)

state = False

for i in range(9):
  if (i+1) % M == 0:
    state = True
  dp[0][i] = (i+1) % M


for i in range(1, N):
  for j in range(9):
    # digit = i+1
    num = j+1
    if (dp[i-1][j]*10+num) % M == 0:
      state = True
    dp[i][j] = (dp[i-1][j]*10+num) % M

# print(dp)

if not state:
  print(-1)
  exit()

for i in range(N-1, -1, -1):
  for j in range(8, -1, -1):
    if dp[i][j] == 0:
      digit = i+1
      num = j+1
      ans_li = []
      for i in range(digit):
        ans_li.append(str(num))
      ans = int(''.join(ans_li))
      print(ans)
      exit()