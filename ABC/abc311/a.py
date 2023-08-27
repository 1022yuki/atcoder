N = int(input())
S = input()

fa = False
fb = False
fc = False

for i in range(N):
    if S[i] == 'A':
        fa = True
    elif S[i] == 'B':
        fb = True
    elif S[i] == 'C':
        fc = True
    if fa and fb and fc:
        print(i+1)
        exit()