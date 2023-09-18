# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import defaultdict

def solution(A):
    # Implement your solution here
    len_a = len(A)
    Sum = []
    for i in range(len_a-1):
        Sum.append(A[i]+A[i+1])
    
    ans = 0
    last = -1
    dic = defaultdict(int)
    for i in range(len_a-1):
        num = Sum[i]
        if num == last:
            last = -1
        else:
            dic[num] += 1
            last = num
            if dic[num] > ans:
                ans = dic[num]
    return ans

A = [10,1,3,1,2,2,1,0,4]
A = [5,3,1,3,2,3]
A = [9,9,9,9,9]
A = [1,5,2,4,3,3]
print(solution(A))