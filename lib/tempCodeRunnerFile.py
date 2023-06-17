
a = list(range(n))
while True:
    print(a)
    if not next_permutation(a, 0, n):
        break
