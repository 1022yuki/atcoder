n, m1, m2, m3, m4 = map(int, input().split())

def size(height: int) -> str:
    if m1<=height and height<m2:
        return 'S'
    elif m2<=height and height<m3:
        return 'M'
    elif m3<=height and height<m4:
        return 'L'
    else:
        return 'X'

S = []
D = []
for i in range(n):
    s, d = map(str, input().split())
    S.append(s)
    D.append(int(d))

Ans_s = []
Ans_m = []
Ans_l = []
Ans_x = []
for i in range(n):
    si = size(D[i])
    if si == 'S':
        Ans_s.append(S[i])
    elif si == 'M':
        Ans_m.append(S[i])
    elif si == 'L':
        Ans_l.append(S[i])
    else:
        Ans_x.append(S[i])

print('S:')
for i in range(len(Ans_s)):
    print(Ans_s[i])

print('M:')
for i in range(len(Ans_m)):
    print(Ans_m[i])

print('L:')
for i in range(len(Ans_l)):
    print(Ans_l[i])

print('X:')
for i in range(len(Ans_x)):
    print(Ans_x[i])