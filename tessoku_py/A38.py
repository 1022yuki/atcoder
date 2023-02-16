D, N = map(int, input().split())

W = [0] + [24]*D
I = []
for i in range(N):
  l, r, h = map(int, input().split())
  I.append([h, l, r])

I.sort()

# print(I)

for i in range(N):
  h, l, r = I[i]
  for j in range(l, r+1):
    W[j] = min(W[j], h)

# print(W)
print(sum(W))