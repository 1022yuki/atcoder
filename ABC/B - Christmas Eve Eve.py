N = int(input())

P = []

for _ in range(0, N):
  p = int(input())
  P.append(p)

max = max(P)

sum = 0

for i in range(0, N):
  sum += P[i]

for i in range(0, N):
  if P[i] == max:
    sum -= P[i]/2
    break

print(int(sum))