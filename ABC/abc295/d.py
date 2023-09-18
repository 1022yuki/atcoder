S = input()

Sum = []
for i in range(10):
    Sum.append([0])

for i in range(len(S)):
    for j in range(10):
        if j == int(S[i]):
          Sum[j].append((Sum[j][-1]+1)%2)
        else:
          Sum[j].append(Sum[j][-1])

# print(Sum)

from collections import defaultdict
dic = defaultdict(int)
for i in range(len(S)+1):
  num = 0
  for j in range(10):
    num+=Sum[j][i]*(2**j)
  dic[num]+=1

# print(dic)

ans = 0
for val in dic.values():
  ans += val*(val-1)//2
print(ans)