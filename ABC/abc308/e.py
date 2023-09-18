def culc_mex(a, b, c):
    for n in range(0, 4):
        if a!=n and b!=n and c!=n:
            return n

N = int(input())
A = list(map(int, input().split()))
S = input()

sum_m_0 = [0]
sum_m_1 = [0]
sum_m_2 = [0]
sum_x_0 = [0]
sum_x_1 = [0]
sum_x_2 = [0]

# 累積和を作る
for i in range(N):
    if S[i]=='M':
        if A[i]==0:
            sum_m_0.append(sum_m_0[-1]+1)
            sum_m_1.append(sum_m_1[-1])
            sum_m_2.append(sum_m_2[-1])
        if A[i]==1:
            sum_m_0.append(sum_m_0[-1])
            sum_m_1.append(sum_m_1[-1]+1)
            sum_m_2.append(sum_m_2[-1])
        if A[i]==2:
            sum_m_0.append(sum_m_0[-1])
            sum_m_1.append(sum_m_1[-1])
            sum_m_2.append(sum_m_2[-1]+1)
        sum_x_0.append(sum_x_0[-1])
        sum_x_1.append(sum_x_1[-1])
        sum_x_2.append(sum_x_2[-1])
    elif S[i]=='X':
        if A[i]==0:
            sum_x_0.append(sum_x_0[-1]+1)
            sum_x_1.append(sum_x_1[-1])
            sum_x_2.append(sum_x_2[-1])
        if A[i]==1:
            sum_x_0.append(sum_x_0[-1])
            sum_x_1.append(sum_x_1[-1]+1)
            sum_x_2.append(sum_x_2[-1])
        if A[i]==2:
            sum_x_0.append(sum_x_0[-1])
            sum_x_1.append(sum_x_1[-1])
            sum_x_2.append(sum_x_2[-1]+1)
        sum_m_0.append(sum_m_0[-1])
        sum_m_1.append(sum_m_1[-1])
        sum_m_2.append(sum_m_2[-1])
    else:
        sum_m_0.append(sum_m_0[-1])
        sum_m_1.append(sum_m_1[-1])
        sum_m_2.append(sum_m_2[-1])
        sum_x_0.append(sum_x_0[-1])
        sum_x_1.append(sum_x_1[-1])
        sum_x_2.append(sum_x_2[-1])

# print(sum_m_0)
# print(sum_m_1)
# print(sum_m_2)
# print(sum_x_0)
# print(sum_x_1)
# print(sum_x_2)

ans = 0

for i in range(N):
    if S[i]=='E':
        b = A[i]
        ans += (sum_m_0[i+1]-sum_m_0[0])*(sum_x_0[N]-sum_x_0[i])*culc_mex(0, b, 0)
        ans += (sum_m_0[i+1]-sum_m_0[0])*(sum_x_1[N]-sum_x_1[i])*culc_mex(0, b, 1)
        ans += (sum_m_0[i+1]-sum_m_0[0])*(sum_x_2[N]-sum_x_2[i])*culc_mex(0, b, 2)  
        ans += (sum_m_1[i+1]-sum_m_1[0])*(sum_x_0[N]-sum_x_0[i])*culc_mex(1, b, 0)
        ans += (sum_m_1[i+1]-sum_m_1[0])*(sum_x_1[N]-sum_x_1[i])*culc_mex(1, b, 1)
        ans += (sum_m_1[i+1]-sum_m_1[0])*(sum_x_2[N]-sum_x_2[i])*culc_mex(1, b, 2)
        ans += (sum_m_2[i+1]-sum_m_2[0])*(sum_x_0[N]-sum_x_0[i])*culc_mex(2, b, 0)
        ans += (sum_m_2[i+1]-sum_m_2[0])*(sum_x_1[N]-sum_x_1[i])*culc_mex(2, b, 1)
        ans += (sum_m_2[i+1]-sum_m_2[0])*(sum_x_2[N]-sum_x_2[i])*culc_mex(2, b, 2)

print(ans)