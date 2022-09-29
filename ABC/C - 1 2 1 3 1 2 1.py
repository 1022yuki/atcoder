N = int(input())

S = [[1]]

for i in range(N-1):
  s = S[-1] + [i+2] + S[-1]
  S.append(s)

ans = S[-1]

print(*ans)