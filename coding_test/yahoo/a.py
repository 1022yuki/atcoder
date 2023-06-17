n = int(input())
a = list(map(int, input().split()))

a.sort()
min = a[0]
max = a[-1]

print(min, max)
print("".join(map(str, a)))