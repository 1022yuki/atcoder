# https://note.nkmk.me/python-union-find/

from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return
        
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def size(self, x):
        return -self.parents[self.find(x)]
        
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())
    
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
    
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

N, K, L = map(int, input().split())

uf_road = UnionFind(N)
uf_rail = UnionFind(N)

for i in range(K):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    uf_road.union(p, q)

for i in range(L):
    r, s = map(int, input().split())
    r -= 1
    s -= 1
    uf_rail.union(r, s)

from collections import defaultdict
dic = defaultdict(int)

for i in range(N):
    dic[uf_road.find(i), uf_rail.find(i)]+=1

ans = []
for i in range(N):
    ans.append(dic[uf_road.find(i), uf_rail.find(i)])

print(*ans)