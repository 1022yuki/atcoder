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


from collections import defaultdict
N = int(input())

dic = defaultdict(int)
pts = set()
X = []
Y = []
for i in range(N):
    x,y = map(int,input().split())
    pts.add((x,y))
    dic[(x,y)] = i
    X.append(x)
    Y.append(y)

uf = UnionFind(N)

for i in range(N):
    x, y = X[i], Y[i]
    dif = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)]
    for dx,dy in dif:
        nx, ny = x+dx, y+dy
        if (nx,ny) in pts:
            uf.union(i,dic[(nx,ny)])
            
  
# print(uf.all_group_members())
print(uf.group_count())