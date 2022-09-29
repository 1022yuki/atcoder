import math

N = int(input())

ans = 0

for A in range(1, N):
  if N%A != 0:
    num = math.floor(N/A)
  else:
    num = N//A -1
  ans += num

print(ans)