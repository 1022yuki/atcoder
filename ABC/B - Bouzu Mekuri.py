N = int(input())
S = list(input())

for i in range(N):
  if S[i] == "1":
    t = i
    break

if t % 2 == 0:
  print('Takahashi')
else:
  print('Aoki')