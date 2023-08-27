A, B = map(int, input().split())

if A+1==B and A%3!=0:
    print('Yes')
    exit()

# if A+3==B:
#     print('Yes')
#     exit()

print('No')