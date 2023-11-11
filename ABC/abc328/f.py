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

N, Q = map(int, input().split())

Qs = []
for i in range(Q):
  a, b, d = map(int, input().split())
  Qs.append([a, b, d])

X = [0]*N
uf = UnionFind(N)

ans = []

for i in range(Q):
  a, b, d = Qs[i]
  a -= 1
  b -= 1
  if a==b and d==0:
    continue
  if uf.same(a, b):
    if not X[b] == X[a]-d:
      continue
  print(i)
  X[b] = X[a]-d
  print(X)
  # print(X[a], X[b], d)
  uf.union(a, b)
  ans.append(i+1)

# print(X)
print(ans)