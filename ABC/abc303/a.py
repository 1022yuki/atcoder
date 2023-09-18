N = int(input())
S = input()
T = input()

flag = True

for i in range(N):
    if S[i]==T[i]:
        continue
    if S[i]=="1" and T[i]=="l":
        continue
    if S[i]=="l" and T[i]=="1":
        continue
    if S[i]=="0" and T[i]=="o":
        continue
    if S[i]=="o" and T[i]=="0":
        continue
    flag = False

if flag:
    print('Yes')
else:
    print('No')