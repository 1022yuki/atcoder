# Union-Find 木
class unionfind:
	# n 頂点の Union-Find 木を作成
	# （ここでは頂点番号が 1-indexed になるように実装しているが、0-indexed の場合は par, size のサイズは n でよい）
	def __init__(self, n):
		self.n = n
		self.par = [ -1 ] * (n + 1) # 最初は親が無い
		self.size = [ 1 ] * (n + 1) # 最初はグループの頂点数が 1
	
	# 頂点 x の根を返す関数
	def root(self, x):
		# 1 個先（親）がなくなる（つまり根に到達する）まで、1 個先（親）に進み続ける
		while self.par[x] != -1:
			x = self.par[x]
		return x
	
	# 要素 u, v を統合する関数
	def unite(self, u, v):
		rootu = self.root(u)
		rootv = self.root(v)
		if rootu != rootv:
			# u と v が異なるグループのときのみ処理を行う
			if self.size[rootu] < self.size[rootv]:
				self.par[rootu] = rootv
				self.size[rootv] += self.size[rootu]
			else:
				self.par[rootv] = rootu
				self.size[rootu] += self.size[rootv]
	
	#  要素 u と v が同一のグループかどうかを返す関数
	def same(self, u, v):
		return self.root(u) == self.root(v)


N, M = map(int, input().split())
road = []
for i in range(M):
  a, b = map(int, input().split())
  road.append((a, b))
Q = int(input())
queries = []
for i in range(Q):
  inp = list(map(int, input().split()))
  queries.append(inp)

uf = unionfind(N)

# 最後に運休になっている路線
cancelled = [False]*(M+1)
for i in range(Q):
  if queries[i][0] == 1:
    x = queries[i][1]
    cancelled[x] = True

for i in range(M):
  a, b = road[i]
  if cancelled[i+1] == False and uf.same(a, b) == False:
    uf.unite(a, b)

ans = []

for i in range(Q-1, -1, -1):
  if queries[i][0] == 1:
    x = queries[i][1]
    a, b = road[x-1]
    uf.unite(a, b)

  if queries[i][0] == 2:
    u, v = queries[i][1:]
    if uf.same(u, v):
      ans.append('Yes')
    else:
      ans.append('No')

# print(ans)
for i in range(len(ans)-1, -1, -1):
  print(ans[i])