T = int(input())
N = int(input())

imos = [0] * (T+1)

for i in range(N):
  l, r = map(int, input().split())
  imos[l] += 1
  imos[r] -= 1

# print(imos)

sum = [0]
for i in range(T):
  sum.append(sum[-1] + imos[i])
  print(sum[-1])