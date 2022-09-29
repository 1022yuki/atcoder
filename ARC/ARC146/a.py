N = int(input())
A = list(map(int, input().split()))

A.sort()

# print(A)

ans1 = str(A[-1]) + str(A[-2]) +str(A[-3])

# print(ans1)

ans2 = str(A[-1]) + str(A[-3]) +str(A[-2])

ans3 = str(A[-2]) + str(A[-1]) +str(A[-3])

ans4 = str(A[-2]) + str(A[-3]) +str(A[-1])

ans5 = str(A[-3]) + str(A[-1]) +str(A[-2])

ans6 = str(A[-3]) + str(A[-2]) +str(A[-1])

ans = max(int(ans1), int(ans2), int(ans3), int(ans4), int(ans5), int(ans6))

print(ans)