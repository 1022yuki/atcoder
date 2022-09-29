n = int(input())

imos = [0] * 1000002
sum = [0] * 1000002

for i in range(n):
  a, b = map(int, input().split())
  imos[a] += 1
  imos[b+1] -= 1

# print(imos)
for i in range(1000001):
  sum[i+1] = sum[i] + imos[i]

print(max(sum))