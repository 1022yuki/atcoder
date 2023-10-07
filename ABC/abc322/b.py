N, M = map(int, input().split())
S = input()
T = input()

isPrefix = False
isSuffix = False

if S == T[:N]:
    isPrefix = True

if S == T[-N:]:
    isSuffix = True

if isPrefix and isSuffix:
    print(0)
elif isPrefix:
    print(1)
elif isSuffix:
    print(2)
else:
    print(3)