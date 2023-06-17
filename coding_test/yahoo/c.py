from collections import defaultdict

N = int(input())
Tmp = list(map(str, input().split()))
n = int(input())

for i in range(n):
    Ans = Tmp.copy()
    l = int(input())
    dic_a = defaultdict(str)
    for j in range(l):
        a, b = map(str, input().split())
        dic_a[a] = b
    for i in range(N):
        word = Tmp[i]
        if word[0] == '#':
            if dic_a[word]=='':
                print('Error: Lack of data')
                break
            else:
                Ans[i] = dic_a[word]
                if i == N-1:
                    print(*Ans)