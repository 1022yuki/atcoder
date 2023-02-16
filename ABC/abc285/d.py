from collections import defaultdict

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

	def all_group_members(self):
		group_members = defaultdict(list)
		for member in range(self.n):
				group_members[self.root(member)].append(member)
		return group_members

from collections import defaultdict
N = int(input())

dic = defaultdict(int)
uf = unionfind(2*N)

S = []
T = []
for i in range(N):
  s, t = map(str, input().split())
  S.append(s)
  T.append(t)
  # dic[s] = 1

all_nm = set(S+T)
# print(all_nm)

num = 0
for un in all_nm:
  dic[un] = num
  num += 1

Sn = []
Tn = []
for i in range(N):
  si, ti = S[i], T[i]
  Sn.append(dic[si])
  Tn.append(dic[ti])

for i in range(N):
  si = Sn[i]
  ti = Tn[i]
  if uf.same(si, ti):
    print('No')
    exit()
  else:
    uf.unite(si, ti)

print('Yes')