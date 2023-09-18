N, M, H, K = map(int, input().split())
S = input()

from collections import defaultdict
item_d = defaultdict(int)
# item = []
for i in range(M):
    x, y = map(int, input().split())
    item_d[(x, y)] = 1

# print(item_d)

nx = 0
ny = 0

hp = H

for i in range(N):
    hp-=1
    if hp<0:
        print('No')
        exit()
    idou = S[i]

    if idou=='R':
        nx+=1
        if item_d[(nx, ny)]==1 and hp<K:
            hp=K
            item_d[(nx, ny)] = 0
    
    if idou=='L':
        nx-=1
        if item_d[(nx, ny)]==1 and hp<K:
            hp=K
            item_d[(nx, ny)] = 0
    
    if idou=='U':
        ny+=1
        if item_d[(nx, ny)]==1 and hp<K:
            hp=K
            item_d[(nx, ny)] = 0
        
    if idou=='D':
        ny-=1
        if item_d[(nx, ny)]==1 and hp<K:
            hp=K
            item_d[(nx, ny)] = 0

print('Yes')