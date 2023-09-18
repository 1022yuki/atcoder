p, q = map(str, input().split())

grid = [0, 3, 4, 8, 9, 14, 23]

if p == 'A':
    left = 0
elif p == 'B':
    left = 1
elif p == 'C':
    left = 2
elif p == 'D':
    left = 3
elif p == 'E':
    left = 4
elif p == 'F':
    left = 5
else:
    left = 6

if q == 'A':
    right = 0
elif q == 'B':
    right = 1
elif q == 'C':
    right = 2
elif q == 'D':
    right = 3
elif q == 'E':
    right = 4
elif q == 'F':
    right = 5
else:
    right = 6

print(abs(grid[right] - grid[left]))