N = int(input())
A = list(map(int, input().split()))

A.sort()

list = []

for i in range(0, N):
  list.append(i+1)

if A == list:
  print('Yes')
else:
  print('No')