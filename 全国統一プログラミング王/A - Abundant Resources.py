N = int(input())
A = list(map(int, input().split()))

# sum: 累積和
sum = [0]
for i in range(N):
  ele = sum[i] + A[i]
  sum.append(ele)

# print(sum)

ans = 0
# i: 連続する区間の数
for i in range(1, N+1):
  ans = 0
  # j: 始点のindex
  for j in range(N-i+1):
    kouho = sum[j+i] - sum[j]
    ans = max(ans, kouho)
  print(ans)