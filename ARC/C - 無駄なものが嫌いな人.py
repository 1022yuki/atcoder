from collections import defaultdict

N, X = map(int, input().split())

# 半分全列挙
# 半分にしてA,Bに格納する
A = []
B = []
for i in range(N):
  w = int(input())
  if i%2 == 0:
    A.append(w)
  else:
    B.append(w)

def has_bit(n, i):
  return n&(1<<i) > 0

dic = defaultdict(int)

for n in range(1<<(len(A))):
  sum = 0
  for i in range(len(A)):
    if has_bit(n, i):
      sum += A[i]
  dic[sum] += 1

ans = 0

for n in range(1<<(len(B))):
  sum = 0
  for i in range(len(B)):
    if has_bit(n, i):
      sum += B[i]
  ans += dic[X-sum]

# print(dic)
print(ans)