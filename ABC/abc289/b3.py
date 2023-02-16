n, m = map(int, input().split())
a = list(map(int, input().split()))
a_set = set(a)
x = [0] * (n)
for i in range(n):
    if (i + 1) in a_set:
        x[i] = (i+1,True)
    else:
        x[i] = (i + 1, False)

print(x)

tmp=[]
ans=[]
for i in range(n):
    if x[i][1]:
        tmp.append(x[i][0])
    else:
        ans.append(x[i][0])
        if tmp:
            ans.extend(list(reversed(tmp)))
            tmp=[]
# ans.extend(list(reversed(tmp)))
print(*ans)