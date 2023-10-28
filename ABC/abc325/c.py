# https://note.nkmk.me/python-union-find/

from collections import defaultdict
import sys
# def input(): return sys.stdin.readline()[:-1]
sys.setrecursionlimit(10**7)
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=0') 

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

H, W = map(int, input().split())

grid = []
for i in range(H):
  grid.append(list(input()))

uf = UnionFind(H*W)

# 縦横斜めにある#は同じグループに属する
for i in range(H):
    for j in range(W):
        if grid[i][j] == '#':
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == '#':
                    uf.union(i*W+j, ni*W+nj)

# print(uf.all_group_members())

# ans = 0
# for group in uf.all_group_members().values():
#     point = group[0]
#     h, w = point//W, point%W
#     # print(h, w)
#     if grid[h][w] == '#':
#         ans += 1
# print(ans)

cnt = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] != '#':
            continue
        if uf.find(i*W+j) == i*W+j:
            cnt += 1
print(cnt)