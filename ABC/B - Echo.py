N = int(input())
S = input()

T1 = ''
T2 = ''

if N % 2 != 0:
  print('No')
else:
  for i in range(0, N//2):
    T1 += S[i]
  for i in range(N//2, N):
    T2 += S[i]
  if T1 == T2:
    print('Yes')
  else:
    print('No')