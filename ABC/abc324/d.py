N = int(input())
S = list(input())

from collections import defaultdict

dics = defaultdict(int)
for i in range(N):
  dics[S[i]] += 1


heiho = []
for i in range(15):
  heiho.append([])
for n in range(10**7):
  nn = n*n
  ln = len(str(nn))
  heiho[ln].append(n*n)


cnt_0 = dics['0']
lenS = len(S)

cnt = 0
ans_set = set()

for n in range(cnt_0+1):
  for i in range(len(heiho[lenS-n])):
    nn = heiho[lenS-n][i]
    dic = defaultdict(int)
    for i in range(len(str(nn))):
      dic[str(nn)[i]] += 1
    flag = True
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
      ans_set.add(nn)
      cnt += 1

print(len(ans_set))