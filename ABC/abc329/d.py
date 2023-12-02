N, M = map(int, input().split())
A = list(map(int, input().split()))

# 得票数が多く、番号が若い人が当選
# 得票数が同じなら、番号が若い人が当選

from collections import defaultdict

dic = defaultdict(int)

Vote = [0]*(N)
# (番号, 得票数) = (0, 0)
champ = [0, 0]
for i in range(M):
  # Vote[A[i]-1] += 1
  # print(Vote)
  dic[A[i]] += 1
  # print(dic)
  if dic[A[i]]>champ[1]:
    champ = [A[i], dic[A[i]]]
  elif dic[A[i]]==champ[1] and A[i]<champ[0]:
    champ = [A[i], dic[A[i]]]
  print(champ[0])