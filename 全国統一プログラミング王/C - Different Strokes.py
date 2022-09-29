from ipaddress import ip_address


N = int(input())

# A[i]+B[i]の大きい順にソートする
# 配列arrに格納する
arr = []
for i in range(0, N):
  a, b = map(int, input().split())
  arr.append([a+b, a, b])

# arr.sort()
arr.reverse()

print(arr)

# 偶数番目は高橋くん、奇数番目は青木さんがとる
t = 0
a = 0
for i in range(0, N):
  if i % 2 == 0:
    t += arr[i][1]
  else:
    a += arr[i][2]

ans = t - a
print(ans)