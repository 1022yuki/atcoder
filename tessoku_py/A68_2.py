from collections import deque
 
class Dinic:
    def __init__(self, n):
        self.n = n
        self.links = [[] for _ in range(n)]
        self.depth = None
        self.progress = None
 
    def add_link(self, _from, to, cap):
        self.links[_from].append([cap, to, len(self.links[to])])
        self.links[to].append([0, _from, len(self.links[_from]) - 1])
 
    def bfs(self, s):
        depth = [-1] * self.n
        depth[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for cap, to, rev in self.links[v]:
                if cap > 0 and depth[to] < 0:
                    depth[to] = depth[v] + 1
                    q.append(to)
        self.depth = depth
 
    def dfs(self, v, t, flow):
        if v == t:
            return flow
        links_v = self.links[v]
        for i in range(self.progress[v], len(links_v)):
            self.progress[v] = i
            cap, to, rev = link = links_v[i]
            if cap == 0 or self.depth[v] >= self.depth[to]:
                continue
            d = self.dfs(to, t, min(flow, cap))
            if d == 0:
                continue
            link[0] -= d
            self.links[to][rev][0] += d
            return d
        return 0
 
    def max_flow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            if self.depth[t] < 0:
                return flow
            self.progress = [0] * self.n
            current_flow = self.dfs(s, t, float('inf'))
            while current_flow > 0:
                flow += current_flow
                current_flow = self.dfs(s, t, float('inf'))
 
# 使い方
# mf = Dinic(6)
# mf.add_link(0, 1, 10)
# mf.add_link(0, 3, 4)
# mf.add_link(1, 2, 9)
# mf.add_link(1, 4, 6)
# mf.add_link(2, 5, 8)
# mf.add_link(3, 4, 3)
# mf.add_link(4, 5, 4)
# print(mf.max_flow(0, 5))

N, M = map(int, input().split())
mf = Dinic(N)

for i in range(M):
  a, b, c = map(int, input().split())
  a -= 1
  b -= 1
  mf.add_link(a, b, c)

ans = mf.max_flow(0, N-1)
print(ans)