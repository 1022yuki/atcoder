A, B, K = map(int, input().split())

slime = A
shout = 0

while (slime < B):
  slime *= K
  shout += 1

print(shout)