# https://note.nkmk.me/python-union-find/
import sys
def input(): return sys.stdin.readline()[:-1]
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

uf = UnionFind(N)

for i in range(M):
    u, v = map(int, input().split())
    u-=1
    v-=1
    uf.union(u, v)

K = int(input())
X = []
Y = []
for i in range(K):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

O = int(input())
P = []
Q = []
for i in range(O):
    p, q = map(int, input().split())
    P.append(p)
    Q.append(q)

# print(uf)

dic = defaultdict(int)

for i in range(K):
    x = X[i]
    y = Y[i]
    x-=1
    y-=1
    par_x = uf.find(x)
    par_y = uf.find(y)
    if par_x>par_y:
        par_x, par_y = par_y, par_x
    dic[(par_x, par_y)] = 1

for i in range(O):
    p = P[i]
    q = Q[i]
    p-=1
    q-=1
    par_p = uf.find(p)
    par_q = uf.find(q)
    if par_p>par_q:
        par_p, par_q = par_q, par_p
    if dic[(par_p, par_q)]==1:
        print('No')
    else:
        print('Yes')