from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)

N, T = map(int, input().split())

dic = defaultdict(list)
for i in range(N-1):
  jousi, buka = map(int, input().split())
  dic[jousi].append(buka)
  dic[buka].append(jousi)

# print(dic)

inf = 10**10

revel = [-inf]*(N+1)

# i番目の社員のレベルを返す(配列revelを埋めながら)
def rec(i, pi):
  if revel[i] != -inf:
    return revel[i]
  ret = -inf
  cnt = 0
  for ni in dic[i]:
    if ni != pi:
      ret = max(ret, rec(ni, i)+1)
      cnt += 1
  # 自分がきた頂点以外の頂点がなかったら頂点以外の頂点がなかったらレベル0
  # 普通に配列の長さが1で良かった気がする
  if cnt == 0:
    revel[i] = 0
    return 0
  revel[i] = ret
  return ret

# 社長から呼び出す
rec(T, 0)

print(*revel[1:])