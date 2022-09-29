N = list(input())
# print(N)

ans = 0
for i in range(len(N)):
  posi = len(N)-i-1
  ans += int(N[posi]) * 2**i

print(ans)