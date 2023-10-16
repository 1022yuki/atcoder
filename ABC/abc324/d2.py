N = int(input())
S = list(input())

from collections import defaultdict

dics = defaultdict(int)
for i in range(N):
  dics[S[i]] += 1

heiho = []
for n in range(4*(10**6)-8*(10**5)):
  heiho.append(n*n)

# print(heiho[-1])

ans_set = set()
for i in range(4*(10**6)-8*(10**5)):
  dic = defaultdict(int)
  flag = True
  for j in range(len(str(heiho[i]))):
    dic[str(heiho[i])[j]] += 1
  for dig in range(10):
    if dig==0:
      if dic['0'] > dics['0']:
        flag = False
        break
    else:
      if dic[str(dig)] != dics[str(dig)]:
        flag = False
        break
  if flag:
    ans_set.add(heiho[i])

# print(ans_set)
print(len(ans_set))