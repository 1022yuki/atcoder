# flagによってYesとNoを出力
def op(flag):
    if flag:
        print('Yes')
    else:
        print('No')

N, A, B = map(int, input().split())
C = list(map(int, input().split()))

ans = A+B

for i in range(len(C)):
    if C[i]==ans:
        print(i+1)
        exit()