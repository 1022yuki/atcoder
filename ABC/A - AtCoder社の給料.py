N = int(input())

sum = 0

for i in range(0, N):
  sum += 10000 * (i+1) / N

print(int(sum))