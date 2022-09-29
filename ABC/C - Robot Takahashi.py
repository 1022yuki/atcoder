from collections import defaultdict


N = int(input())
S = input()
W = list(map(int, input().split()))

adult = []
child = []
for i in range(N):
  if S[i] == '1':
    adult.append(W[i])
  else:
    child.append(W[i])

adult.sort()
child.sort()

dict_adult = defaultdict(int)
dict_child = defaultdict(int)

for x in adult:
  dict_adult[x] += 1

for x in child:
  dict_child[x] += 1

all = adult + child
all.sort()

dict_all = defaultdict(int)

for x in all:
  dict_all[x] += 1

# print(dict_adult)
# print(dict_child)
# print(dict_all)

ans = len(adult)
sum = ans
for key in dict_all.keys():
  sum += dict_child[key]
  sum -= dict_adult[key]
  ans = max(ans, sum)

print(ans)