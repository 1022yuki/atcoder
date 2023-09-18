W, H = map(int, input().split())
N = int(input())

P = []
Q = []
for i in range(N):
    p, q = map(int, input().split())
    P.append(p)
    Q.append(q)

a = int(input())
A = list(map(int, input().split()))
b = int(input())
B = list(map(int, input().split()))

import bisect
from collections import defaultdict

dic = defaultdict(int)

for i in range(N):
    ind_i = bisect.bisect_left(A, P[i])
    ind_j = bisect.bisect_left(B, Q[i])
    dic[(ind_i, ind_j)] += 1

# print(dic)

nums = []
for key, value in dic.items():
    nums.append(value)

# print(nums)
if len(nums)!=(a+1)*(b+1):
    print(0, max(nums))
else:
    print(min(nums), max(nums))