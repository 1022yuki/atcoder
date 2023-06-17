N = int(input())

a = N//5

b = 5*a
c = 5*(a+1)

if N-b < c-N:
    print(b)
else:
    print(c)