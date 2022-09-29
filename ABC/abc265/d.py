from collections import defaultdict

N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

# 累積和の配列
sum = [0]
for i in range(N):
  sum.append(sum[i] + A[i])

print(sum)

dict = defaultdict(int)

for x in sum:
  dict[x] += 1

# print(dict)

for i in range(N):
  bor_1 = sum[i]

  if dict[bor_1+P] == 1:
    if dict[bor_1+P+Q] == 1:
      if dict[bor_1+P+Q+R] == 1:
        print('Yes')
        exit()

print('No')