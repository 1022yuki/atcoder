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

N, M = map(int, input().split())

edges = []
for i in range(N):
  edges.append([])

uf = UnionFind(N)

dic = defaultdict(int)

U = []
for i in range(M):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  U.append(u)
  uf.union(u, v)
  dic[u] += 1
  dic[v] += 1

# print(uf.all_group_members())

numV = [0]*N
numE = [0]*N
for i in range(N):
    numV[uf.find(i)]+=1
for i in range(M):
    numE[uf.find(U[i])]+=1

for i in range(N):
    if numV[i]:
        if numV[i]!=numE[i]:
            print("No")
            exit()

print("Yes")

# for ro in uf.all_group_members():
#   mem = uf.members(ro)
#   # print(mem)
#   v_num = len(mem)
#   ed = 0
#   for v in mem:
#     ed += dic[v]
#   if not v_num*2==ed:
#     print("No")
#     exit()

# print("Yes")