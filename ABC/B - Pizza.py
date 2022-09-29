N = int(input())

A = list(map(int, input().split()))

ANG = [0]

sum = 0

for a in A:
  sum += a
  ANG.append(sum % 360)

# print(ANG)
sortedANG = ANG.sort()
# print(ANG)

DIFANG = []

for i in range(0, N):
  dif = ANG[i+1] - ANG[i]
  DIFANG.append(dif)

DIFANG.append(360-ANG[N])

# print(DIFANG)

print(max(DIFANG))