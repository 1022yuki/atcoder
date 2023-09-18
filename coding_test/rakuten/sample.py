def solution(A):
    for i in range(0, 10**7+1):
        if i not in A:
            return i
    pass