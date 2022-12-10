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

from collections import defaultdict

N = int(input())

A = []
B = []

set = set()


for i in range(N):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)
  set.add(a)
  set.add(b)

# print(set)
dic = defaultdict(int)
dic[1] = 1

num = 2
for x in set:
  if x != 1:
    dic[x] = num
    num += 1

# print(dic)

uf = unionfind(3*N)

ver_li = [1]
for i in range(N):
  u_a = A[i]
  u_b = B[i]
  # print(u_a)
  # print(u_b)
  uf.unite(dic[u_a], dic[u_b])

ans = 1
for x in set:
  # print(x)
  v_num = dic[x]
  # print(v_num)
  # print()
  if uf.same(1, v_num):
    ans = max(ans, x)

print(ans)