N = int(input())
# N, M = map(int, input().split())
P = list(map(int, input().split()))

max_p = max(P)

# if max_p == P[0]:
#     ans = 0
# else:
#   ans = max(0, max_p-P[0]+1)
# print(ans)

if max_p == P[0]:
    if P.count(max_p) == 1:
        print(0)
        exit()
    else:
        print(1)
        exit()

p = P[0]

while P[0]<=max_p:
    P[0] += 1

print(P[0]-p)