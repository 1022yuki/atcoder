def f(a, b):
    if b==0:
        return a
    else:
        return f(b, a%b)

print(f(10, 2))