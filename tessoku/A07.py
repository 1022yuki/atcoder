D = int(input())
N = int(input())

imos = [0] * (D+1)
imos_sum = [0]

for i in range(N):
  l, r = map(int, input().split())
  imos[l-1] += 1
  imos[r] -= 1

# print(imos)

for d in range(D):
  imos_sum.append(imos_sum[-1]+imos[d])
  print(imos_sum[-1])