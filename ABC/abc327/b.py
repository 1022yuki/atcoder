B = int(input())

for n in range(1, 17):
  if n**n == B:
    print(n)
    exit()

print(-1)