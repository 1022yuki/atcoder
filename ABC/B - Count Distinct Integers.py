N = int(input())

a = list(map(int, input().split()))

# print(a)

count = N

for i in range(0, N):
  for j in range(i+1, N):
    if a[i] == a[j]:
      count -= 1

print(count)