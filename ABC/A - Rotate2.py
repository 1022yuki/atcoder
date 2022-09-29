S = list(input())

S[0], S[1], S[2] = S[1], S[2], S[0]

print(S[0]+S[1]+S[2])