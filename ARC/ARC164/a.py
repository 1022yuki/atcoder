def solve(n, k):
    beki = 38
    while k >= 0 and beki >= 0:
        # print(n, k)
        if n==0 and k==0:
            return 'Yes'
        if n // (3**beki) > 0:
            n -= 3**beki
            k -= 1
        else:
            beki -= 1
    return 'No'

T = int(input())

for i in range(T):
    n, k = map(int, input().split())
    print(solve(n, k))