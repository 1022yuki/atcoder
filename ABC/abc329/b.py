N = int(input())
A = list(map(int, input().split()))

na = list(set(A))
na.sort()
print(na[-2])