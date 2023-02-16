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
if M == 0:
  li = []
  for i in range(1, N+1):
    li.append(i)
  # print("AAAAAAA")
  print(*li)
  exit()

A = list(map(int, input().split()))

li = []
for i in range(1, N+1):
  li.append(i)

uf = UnionFind()

for x in A:
  uf.union(x, x-1)

for i in range(N):
  uf.union(i, i+1000)

# print(uf.all_group_members())

ans = []

for rot in uf.all_group_members():
  # print(rot)
  # print(uf.members(rot))
  a_li = list(uf.members(rot))
  a_li.sort()
  lg = len(a_li)
  a_li = a_li[:(lg//2)]
  for i in range(lg//2):
    a_li[i] += 1
  a_li.reverse()
  # print(a_li)
  ans.append(a_li)
  # print(*a_li, end=" ")
# print()
# print(ans)
ans.sort()

ans2 = []
for i in range(len(ans)):
  ans2 += ans[i]

print(*ans2)