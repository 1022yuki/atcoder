N, X = map(int, input().split())
A = list(map(int, input().split()))

for n in range(101):
  c_A = A.copy()
  c_A.append(n)
  c_A.sort()
  pt = sum(c_A[1: N-1])
  if pt >=X:
    print(n)
    exit()

print(-1)