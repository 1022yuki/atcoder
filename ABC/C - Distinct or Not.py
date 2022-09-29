N = int(input())
A = list(map(int, input().split()))

state = True

# for i in range(0, N):
#   for j in range(0, N):
#     if i != j:
#       if A[i] == A[j]:
#         state = False

A.sort()

for i in range(0, N-1):
  if A[i+1] == A[i]:
    state = False

if state:
  print('YES')
else:
  print('NO')