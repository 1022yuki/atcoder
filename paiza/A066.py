N = int(input())

dif = [0]*(10**2)
sum = [0]
for i in range(N):
    a, b = map(int, input().split())
    dif[a-1]+=1
    dif[b]-=1

for i in range(10**2):
    sum.append(sum[-1]+dif[i])

# print(sum)

ans = 0
con = 0
for x in sum:
    if x==0:
        ans = max(ans, con)
        con = 0
    else:
        con += 1

print(ans)