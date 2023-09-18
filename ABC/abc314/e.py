N, M = map(int, input().split())

C = []
P = []
S = []
avg_avg_per_yen = []
ri_avg = []
avg_per_yen = []
for i in range(N):
    inp = list(map(int, input().split()))
    c = inp[0]
    p = inp[1]
    s = inp[2:]
    C.append(c)
    P.append(p)
    S.append(s)
    avg_point = sum(s)/p
    ri_avg.append(avg_point)
    avg_per_yen.append(avg_point/c)
    avg_avg_per_yen.append([avg_point/c, avg_point, c])

ans = 0
avg_avg_per_yen.sort(reverse=True)
print(avg_avg_per_yen)

num_play = int(M/(avg_avg_per_yen[0][1]))
print(num_play)
print(num_play*avg_avg_per_yen[0][2])

ans += num_play*avg_avg_per_yen[0][2]
gap = M - num_play*avg_avg_per_yen[0][1]

print(gap)

if gap==0:
    print(ans)
    exit()

for i in range(N):
    avg_per_yen, avg_point, c = avg_avg_per_yen[i]
    ans += (gap/avg_per_yen)
    # num_gap_play = int(gap/avg_point)
    # if gap>num_gap_play*avg_point:
    #     num_gap_play += 1
    # ans += num_gap_play*c
    print(ans)
