N = int(input())

dists = []
for i in range(N):
    d = int(input())
    dists.append(d)

# print(dists)

max_edge = max(dists)
other_edges_sum = sum(dists) - max_edge

ans_a = sum(dists)
ans_b = 0

if max_edge < other_edges_sum:
    ans_b = 0
else:
    ans_b = max_edge - other_edges_sum

print(ans_a)
print(ans_b)