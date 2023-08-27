N = int(input())
A = list(map(int, input().split()))
A.sort()

if N==1:
    print(0)
    exit()

low = sum(A)//N
high_num = sum(A)-low*N

# print(low)
# print(high_num)

to_list = [low]*(N-(high_num))+[low+1]*high_num

# print(A)
# print(to_list)

ans = 0
for i in range(N):
    ans += abs(A[i]-to_list[i])

print(ans//2)