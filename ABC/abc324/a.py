N = int(input())
A = list(map(int, input().split()))

flag = True
for i in range(N-1):
  if A[i]!=A[i+1]:
    flag = False
    break

if flag:
  print('Yes')
else:
  print('No')