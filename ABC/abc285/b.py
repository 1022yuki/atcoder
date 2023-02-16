N = int(input())
S = input()

for i in range(1, N):
  cnt = 0
  for fir in range(N-i):
    if S[fir] == S[fir+i]:
      break
    cnt += 1
  print(cnt)