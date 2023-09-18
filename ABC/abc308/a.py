S = list(map(int, input().split()))

for i in range(len(S)):
    n = S[i]
    if n<100 or n>675:
        print('No')
        exit()
    if n%25!=0:
        print('No')
        exit()
    if i != len(S)-1:
        if S[i]>S[i+1]:
            print('No')
            exit()

print('Yes')