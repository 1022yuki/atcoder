from collections import defaultdict

S = list(input())

dict = defaultdict(int)

for x in S:
  dict[x] += 1

ans = [-1]

for k, v in dict.items():
  if v == 1:
    ans.append(k)

print(ans[-1])