D = int(input())
N = int(input())

imos = [0] * (D+2)
imos_sum = [0]

for i in range(N):
  l, r = map(int, input().split())
  imos[l] += 1
  imos[r+1] -= 1

for d in range(1, D+1):
  imos_sum.append(imos_sum[-1]+imos[d])

for d in range(1, D+1):
  print(imos_sum[d])