from collections import defaultdict

N = int(input())

dic = defaultdict(list)
Ice = []
for i in range(N):
    f, s = map(int, input().split())
    Ice.append([s, f])
    dic[f].append(s)

Ice.sort(reverse=True)

choice1_s = Ice[0][0]
choice1_f = Ice[0][1]

other_s_max = -1
for k, v in dic.items():
    if k == choice1_f:
        continue 
    else:
        other_s_max = max(other_s_max, max(v))

ans = 0
if len(dic[choice1_f])>1:
    li = dic[choice1_f]
    li.sort(reverse=True)
    choice2_s = li[1]
    ans = max(ans, choice1_s + choice2_s//2)

ans = max(ans, choice1_s + other_s_max)
print(ans)