from bisect import bisect_left, bisect_right

N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = bisect_right(A, X)
print(ans)