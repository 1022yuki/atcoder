S = list(input())
K = int(input())

lg = len(S)
dots = 0

R = [-1]*(lg)
ans = 0
for i in range(lg):
    if i==0:
      R[i] = 0
    else:
      R[i] = R[i-1]
      if S[i-1]=='.' and dots>0:
         dots-=1
    while R[i]+1<lg:
        if dots==K:
           break
        if S[R[i]+1]=='.':
            if dots+1<=K:
              dots+=1
              R[i]+=1
        else:
           R[i]+=1
    # print(R[i]-i+1)
    ans = max(ans,R[i]-i+1)

print(R)
print(ans)