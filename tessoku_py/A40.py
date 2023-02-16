from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

dic = defaultdict(int)

for i in range(N):
  dic[A[i]] += 1

# print(dic)

ans = 0
for key, value in dic.items():
  ans += value*(value-1)*(value-2)//6

print(ans)