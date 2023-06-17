N = int(input())
A = list(map(int, input().split()))

if N==1:
    print('Yes')
    exit()

A.sort()

small = A[:N//2]
mid = A[N//2]
big = A[(N//2)+1:]

# print(small)
# print(mid)
# print(big)

# if max(small)==min(big):
#     print('No')
#     exit()
if max(small)==min(big) and small.count(max(small))+big.count(min(big))>=N//2:
  print('No')
  exit()

if mid < max(big):
    print('Yes')
else:
    print('No')