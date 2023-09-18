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

N = int(input())

City_x = []
City_y = []
for i in range(N):
    x, y = map(int, input().split())
    City_x.append((x, y, i))
    City_y.append((y, x, i))

City_x.sort()
City_y.sort()
# print(City_x)
# print(City_y)

edges = []
for i in range(N-1):
    dif_x = City_x[i+1][0]-City_x[i][0]
    edges.append((dif_x, City_x[i][2], City_x[i+1][2]))
    dif_y = City_y[i+1][0]-City_y[i][0]
    edges.append((dif_y, City_y[i][2], City_y[i+1][2]))

edges.sort()
# print(edges)

uf = UnionFind(N)
ans = 0

for i in range(2*(N-1)):
    cost, a, b = edges[i]
    if not uf.same(a, b):
        uf.union(a, b)
        ans += cost

print(ans)