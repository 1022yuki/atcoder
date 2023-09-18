S = list(input())

def is_palindrome(S):
    for i in range(len(S)//2):
        if S[i] != S[-i-1]:
            return False
    return True

ans = 1
for i in range(len(S)):
    for j in range(i+1, len(S)):
        if is_palindrome(S[i:j+1]):
            ans = max(ans, j-i+1)

print(ans)