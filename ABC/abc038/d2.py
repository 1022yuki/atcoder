# 区間max
# セグメント木（ここでは書籍とは異なり、pos が 0-indexed になるように実装しています）
class segtree:
	# 要素 dat の初期化を行う（最初は全部ゼロ）
	def __init__(self, n):
		self.size = 1
		while self.size < n:
			self.size *= 2
		self.dat = [ 0 ] * (self.size * 2)
	
	# クエリ 1 に対する処理
	def update(self, pos, x):
		pos += self.size # pos は 0-indexed なので、A[pos] のみに対応するセルの番号は pos + size
		self.dat[pos] = x
		while pos >= 2:
			pos //= 2
			self.dat[pos] = max(self.dat[pos * 2], self.dat[pos * 2 + 1])
	
	# クエリ 2 に対する処理
	# u は現在のセル番号、[a, b) はセルに対応する半開区間、[l, r) は求めたい半開区間
	# sg_t.query(0, 10**5+1, 0, sg_t.size, 1)
	def query(self, l, r, a, b, u):
		if r <= a or b <= l:
			return -1000000000 # 一切含まれない場合
		if l <= a and b <= r:
			return self.dat[u] # 完全に含まれる場合
		m = (a + b) // 2
		answerl = self.query(l, r, a, m, u * 2)
		answerr = self.query(l, r, m, b, u * 2 + 1)
		return max(answerl, answerr)

N = int(input())
Bs = []
# 横は小さい順、縦は大きい順にソート
for i in range(N):
    w, h = map(int, input().split())
    h*=-1
    Bs.append([w, h])
Bs.sort()


sg_t = segtree((10**5)+1)

for w, h in Bs:
    h*=-1
    update = sg_t.query(0, h, 0, sg_t.size, 1)
    update += 1
    sg_t.update(h, update)

ans = sg_t.query(0, 10**5+1, 0, sg_t.size, 1)
print(ans)