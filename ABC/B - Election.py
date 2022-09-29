N = int(input())

S = []

for _ in range(0, N):
  s = input()
  S.append(s)

COUNT = []

for i in range(0,N):
  count = S.count(S[i])
  COUNT.append(count)

for i in range(0,N):
  count = S.count(S[i])
  if count == max(COUNT):
    print(S[i])
    break