N, L, R = map(int, input().split())
A = list(map(int, input().split()))

sum_a = [0]
for i in range(N):
  sum_a.append(sum_a[-1]+A[i])

# print(A)
# print(sum)

maxlval = 0
for i in range(N):
  # 左側1,2,..iの和
  l_sum = sum_a[i+1]
  # print(l_sum)
  value_l = l_sum - L*(i+1)
  maxlval = max(maxlval, value_l)

left = 0
for i in range(N):
  l_sum = sum_a[i+1]
  value_l = l_sum - L*(i+1)
  # print(value_l)
  if value_l == maxlval and maxlval != 0:
    left = i+1
    break

# print(left)
# left分配列Aの左からLにする
for i in range(left):
  A[i] = L

# もう一度累積和を作る
sum_a = [0]
for i in range(N):
  sum_a.append(sum_a[-1]+A[i])

maxrval = 0
for i in range(N):
  # 右側1,2,..iの和
  r_sum = sum_a[-1] - sum_a[N-i-1]
  # print(r_sum)
  value_r = r_sum - R*(i+1)
  # print(value_r)
  maxrval = max(maxrval, value_r)

right = 0
for i in range(N):
  r_sum = sum_a[-1] - sum_a[N-i-1]
  value_r = r_sum - R*(i+1)
  if value_r == maxrval and maxrval != 0:
    right = i+1
    break

# print(right)

for i in range(right):
  A[N-1-i] = R

print(left)
print(right)

print(A)
print(sum(A))