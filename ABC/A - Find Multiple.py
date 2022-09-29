import sys

A, B, C = map(int, input().split())

for i in range(0, 1000):
  if A <= C*i <= B:
    print(C*i)
    sys.exit()

print(-1)
