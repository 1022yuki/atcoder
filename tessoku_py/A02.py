N, X = map(int, input().split())
A = list(map(int, input().split()))

for x in A:
  if x == X:
    print('Yes')
    exit()

print('No')