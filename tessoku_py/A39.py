N = int(input())

RL = []
for i in range(N):
  l, r = map(int, input().split())
  RL.append([r, l])

RL.sort()

ans = 0
last = 0
for r, l in RL:
  if l >= last:
    # print(l, r)
    ans += 1
    last = r

print(ans)