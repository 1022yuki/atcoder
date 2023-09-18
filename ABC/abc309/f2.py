# 区間max
# セグメント木（ここでは書籍とは異なり、pos が 0-indexed になるように実装しています）
class segtree:
	# 要素 dat の初期化を行う（最初は全部ゼロ）
	def __init__(self, n):
		self.size = 1
		while self.size < n:
			self.size *= 2
		self.dat = [ 10**9+10 ] * (self.size * 2)
	
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
	def query(self, l, r, a, b, u):
		if r <= a or b <= l:
			return 1000000000 # 一切含まれない場合
		if l <= a and b <= r:
			return self.dat[u] # 完全に含まれる場合
		m = (a + b) // 2
		answerl = self.query(l, r, a, m, u * 2)
		answerr = self.query(l, r, m, b, u * 2 + 1)
		return min(answerl, answerr)

from collections import defaultdict
N = int(input())
Bs = []
W = []
dic = defaultdict(int)
# hは小さい順、w,dは大きい順にソート
for i in range(N):
	li = list(map(int, input().split()))
	li.sort()
	W.append(li[1])
	li[1]*=-1
	li[2]*=-1
	Bs.append(li)

Bs.sort()
w_ind = list(set(W))
w_ind.sort()
for i in range(len(w_ind)):
	dic[w_ind[i]] = i
	
# print(Bs)
# print(dic)

sg_t = segtree((2*(10**5))+1)

for h, w, d in Bs:
	w*=-1
	d*=-1
	if sg_t.query(0, dic[w], 0, sg_t.size, 1)<d:
		print('Yes')
		exit()
	sg_t.update(dic[w], min(sg_t.query(dic[w], dic[w]+1, 0, sg_t.size, 1), d))

print('No')	