N = int(input())
A = list(map(int, input().split()))

A.sort()
# print(A)

for i in range(N-1):
    # print(A[i], A[i+1])
    if A[i]+1!=A[i+1]:
        print(A[i]+1)