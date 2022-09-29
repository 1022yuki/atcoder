import math
N = int(input())

ans = 0
for i in range(60):
  if 2**i > N:
    break
  ans = i

print(ans)