N = int(input())

W = list(map(str, input().split()))

tar = set(("and", "not", "that", "the", "you"))

for i in range(N):
  if W[i] in tar:
    print("Yes")
    exit()

print("No")