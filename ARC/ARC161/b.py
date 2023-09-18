T = int(input())

def solve(n: int):
    if n<7:
        return -1
    else:
        for i in range(100):
            if n//2**i==0:
                bin_dig = i
                break
        # print(bin_dig)
        cnt_1 = 0
        for i in range(bin_dig-1, -1, -1):
            dig_num

for i in range(T):
    n = int(input())
    print(solve(n))