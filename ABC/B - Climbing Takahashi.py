N = int(input())
H = list(map(int, input().split()))

state = H[0]

for i in range(0, N-1):
  if H[i] < H[i+1]:
    state = H[i+1]
  else:
    break

print(state)