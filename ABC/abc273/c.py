from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
A.sort()
A.reverse()

dict = defaultdict(int)
for x in A:
  dict[x] += 1

# print(A)
# print(dict)

ans = []

for value in dict.values():
  ans.append(value)

# print(ans)

leng = len(ans)

for i in range(N):
  if i < leng:
    print(ans[i])
  else:
    print(0)