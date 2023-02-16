import collections
class UnionFind():
    def __init__(self):
        '''
        unionfind経路圧縮あり,要素にtupleや文字列可,始めに要素数指定なし
        '''
        self.parents = dict()                                      # {子要素:親ID,}
        self.members_set = collections.defaultdict(lambda : set()) # keyが根でvalueが根に属する要素要素(tupleや文字列可)
        self.roots_set = set()                                     # 根の集合(tupleや文字列可)
        self.key_ID = dict()                                       # 各要素にIDを割り振る
        self.ID_key = dict()                                       # IDから要素名を復元する
        self.cnt = 0                                               # IDのカウンター

    def dictf(self,x): # 要素名とIDをやり取りするところ
        if x in self.key_ID:
            return self.key_ID[x]
        else:
            self.cnt += 1
            self.key_ID[x] = self.cnt
            self.parents[x] = self.cnt
            self.ID_key[self.cnt] = x
            self.members_set[x].add(x)
            self.roots_set.add(x)
            return self.key_ID[x]

    def find(self, x):
        ID_x = self.dictf(x)
        if self.parents[x] == ID_x:
            return x
        else:
            self.parents[x] = self.key_ID[self.find(self.ID_key[self.parents[x]])]
            return self.ID_key[self.parents[x]]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        if x == y:
            return
        for i in self.members_set[y]:
            self.members_set[x].add(i)
        self.members_set[y] = set()
        self.roots_set.remove(y)
        self.parents[y] = self.key_ID[x]

    def size(self, x):#xが含まれる集合の要素数
        return len(self.members_set[self.find(x)])

    def same(self, x, y):#同じ集合に属するかの判定
        return self.find(x) == self.find(y)

    def members(self, x):#xを含む集合の要素
        return self.members_set[self.find(x)]

    def roots(self):#根の要素
        return self.roots_set

    def group_count(self):#根の数
        return len(self.roots_set)

    def all_group_members(self):#根とその要素
        return {r: self.members_set[r] for r in self.roots_set}


N, M = map(int, input().split())

edges = []
# for i in range(N):
#   edges.append([])
for i in range(M):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  # edges[a].append(b)
  # edges[b].append(a)
  edges.append((a, b))

Q = int(input())
queries = []
for i in range(Q):
  query = list(map(str, input().split()))
  queries.append(query)

uf = UnionFind()

# 最後まで運休にならない線路は最初にuniteしておく
stop = [False]*M
for i in range(Q):
  query = queries[i]
  if query[0] == "1":
    # print(query[1])
    x = int(query[1])
    x -= 1
    stop[x] = True
for i in range(M):
  if stop[i] == False:
    uf.union(edges[i][0], edges[i][1])

# 最後にリバース
ans = []

for i in range(Q-1, -1, -1):
  query = queries[i]
  
  if query[0] == "1":
    x = int(query[1])
    x -= 1
    uf.union(edges[x][0], edges[x][1])
  
  if query[0] == "2":
    u, v = int(query[1]), int(query[2])
    u -= 1
    v -= 1
    if uf.same(u, v):
      ans.append("Yes")
    else:
      ans.append("No")

ans.reverse()
# print(ans)
for i in range(len(ans)):
  print(ans[i])