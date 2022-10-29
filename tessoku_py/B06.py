N = int(input())
A = list(map(int, input().split()))

sum = [0]
for i in range(N):
  sum.append(sum[-1] + A[i])

Q = int(input())
L = []
R = []
for q in range(Q):
  l, r = map(int, input().split())
  L.append(l)
  R.append(r)

for q in range(Q):
  attempt = R[q] - L[q] + 1
  atari = sum[R[q]] - sum[L[q]-1]
  hazure = attempt - atari
  if atari > hazure:
    print('win')
  elif atari < hazure:
    print('lose')
  else:
    print('draw')