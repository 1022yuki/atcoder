N = int(input())
H = list(map(int, input().split()))

ma = -1
for i in range(N):
  ma = max(ma, H[i])
  if ma == H[i]:
    ans = i
    # print(i)

print(ans+1)