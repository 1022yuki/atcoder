N = int(input())
P = list(map(int, input().split()))

rotate = [0] * N

for i in range(N):
  dish = P[i]
  rotate[(dish-i)%N] += 1
  rotate[(dish-i+1)%N] += 1
  rotate[(dish-i-1)%N] += 1

# print(rotate)

print(max(rotate))