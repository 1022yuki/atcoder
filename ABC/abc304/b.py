N = int(input())

if N<10**3:
    print((N//1))
elif N<10**4:
    print(10*(N//10))
elif N<10**5:
    print(100*(N//100))
elif N<10**6:
    print(1000*(N//1000))
elif N<10**7:
    print(10000*(N//10000))
elif N<10**8:
    print(100000*(N//100000))
else:
    print(1000000*(N//1000000))