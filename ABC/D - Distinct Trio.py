import math
import collections

N =int(input())

A = list(map(int, input().split()))

count = collections.Counter(A)

def ncr(n, r):
  return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

# print(count)

# 答えはnC3から被っているものについて引いたもの
# 同じ要素が2つ含まれているもの、3つ含まれているものに分けて処理する
ans = ncr(N, 3)

# 2つ含まれているもの、条件はcountの値が2以上
for i in count.values():
  if i >= 2:
    num = ncr(i, 2) * (N-i)
    ans -= num

# 3つ含まれているもの、条件はcountの値が3以上
for i in count.values():
  if i >= 3:
    ans -= ncr(i, 3)

print(ans)