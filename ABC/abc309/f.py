# 区間min
# セグメント木（ここでは書籍とは異なり、pos が 0-indexed になるように実装しています）
class segtree:
	# 要素 dat の初期化を行う（最初は全部ゼロ）
	def __init__(self, n):
		self.size = 1
		while self.size < n:
			self.size *= 2
		self.dat = [ 10**9 ] * (self.size * 2)
	
	# クエリ 1 に対する処理
	def update(self, pos, x):
		pos += self.size # pos は 0-indexed なので、A[pos] のみに対応するセルの番号は pos + size
		self.dat[pos] = x
		while pos >= 2:
			pos //= 2
			self.dat[pos] = min(self.dat[pos * 2], self.dat[pos * 2 + 1])
	
	# クエリ 2 に対する処理
	# u は現在のセル番号、[a, b) はセルに対応する半開区間、[l, r) は求めたい半開区間
	# sg_t.query(0, 10**5+1, 0, sg_t.size, 1)
	# セル番号は1にすることに注意
	def query(self, l, r, a, b, u):
		if r <= a or b <= l:
			return 1000000000 # 一切含まれない場合
		if l <= a and b <= r:
			return self.dat[u] # 完全に含まれる場合
		m = (a + b) // 2
		answerl = self.query(l, r, a, m, u * 2)
		answerr = self.query(l, r, m, b, u * 2 + 1)
		return min(answerl, answerr)

import sys
def input(): return sys.stdin.readline()[:-1]
# 座圧忘れずに
from collections import defaultdict
N = int(input())

Boxes = []
val = []
for i in range(N):
    x, y, z = map(int, input().split())
    val.append(x)
    val.append(y)
    val.append(z)
    size = [x, y, z]
    size.sort()
    size[1]*=-1
    size[2]*=-1
    Boxes.append((size[0], size[1], size[2]))

# print(Boxes)
Boxes = list(set(Boxes))
Boxes.sort()
# print(Boxes)

# 座圧
val = list(set(val))
val.sort()
dic = defaultdict(int)
for i in range(len(val)):
	dic[val[i]] = i


seg = segtree(((2*10**5)*3)+10)

for a, b, c in Boxes:
	b*=-1
	c*=-1
	if seg.query(0, dic[b], 0, seg.size, 1)<dic[c]:
		print('Yes')
		exit()
	cur = seg.query(dic[b], dic[b]+1, 0, seg.size, 1)
	if cur > dic[c]:
		cur = dic[c]
	seg.update(dic[b], cur)

print('No')