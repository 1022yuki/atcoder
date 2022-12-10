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
			self.dat[pos] = min(self.dat[pos * 2], self.dat[pos * 2 + 1])
	
	# クエリ 2 に対する処理
	# u は現在のセル番号、[a, b) はセルに対応する半開区間、[l, r) は求めたい半開区間
	def query(self, l, r, a, b, u):
		if r <= a or b <= l:
			return 1000000000 # 一切含まれない場合
		if l <= a and b <= r:
			return self.dat[u] # 完全に含まれる場合
		m = (a + b) // 2
		answerl = self.query(l, r, a, m, u * 2)
		answerr = self.query(l, r, m, b, u * 2 + 1)
		return min(answerl, answerr)

import bisect

N, L, R = map(int, input().split())
X = [-10**10]+list(map(int, input().split()))

# 1-index
dp = [10**10]*(N+1)
dp[0] = -10**10
dp[1] = 0
# 0-indexを1-indexにして考えた
Z = segtree(N+1)
Z.update(0, 10**10)
Z.update(1, 0)

# print(X)
for i in range(2, N+1):
  posL = bisect.bisect_left(X, X[i]-R)
  posR = bisect.bisect_right(X, X[i]-L)
  # print((X, X[i]-L))
  # print(posL, posR)
  dp[i] = Z.query(posL, posR, 0, Z.size, 1) + 1
  Z.update(i, dp[i])

# print(dp)
print(dp[N])