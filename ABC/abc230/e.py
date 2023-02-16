import math
N = int(input())

bor = int(N**0.5)

ans = 0
for i in range(1, bor+1):
  ans += N//i

for i in range(1, N//bor):
  left = N//(i+1)+1
  right = N//i
  ans += i*(right-left+1)
  
print(ans)