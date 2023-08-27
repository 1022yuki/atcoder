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

N, M = map(int, input().split())

Roads = []
for i in range(M):
    a, b, m = map(int, input().split())
    a-=1
    b-=1
    Roads.append((m, a, b))

Q = int(input())
Query = []
for i in range(Q):
    v, w = map(int, input().split())
    v-=1
    Query.append((w, v, i))

Roads.sort(reverse=True)
Query.sort(reverse=True)

# print(Roads)
# print(Query)

ans = [-1]*Q

uf = UnionFind(N)

ind_r = 0
ind_q = 0
road_done = False

while ind_q<Q:
    m, a, b = Roads[ind_r]
    w, v, i = Query[ind_q]
    if m>w and road_done==False:
        uf.union(a, b)
        if ind_r<M-1:
            ind_r+=1
        else:
            road_done = True
    else:
        # print(i)
        # print(uf.all_group_members())
        # print(uf.members(v))
        ans[i] = uf.size(v)
        ind_q+=1

for i in range(Q):
    print(ans[i], end='\n')