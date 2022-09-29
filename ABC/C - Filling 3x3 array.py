h1, h2, h3, w1, w2, w3 = map(int, input().split())

count = 0

# (1,1)成分
for i11 in range(1, min(h1,w1)-1):
  # (1,2)成分
  for i12 in range(1, min(h1, w2)-1):
    # (2,1)成分
    for i21 in range(1, min(h2, w1)-1):
      # (2,2)成分
      for i22 in range(1, min(h2, w2)-1):
        # (3,1)成分
        i31 = w1 - i11 - i21
        # (3,2)成分
        i32 = w2 - i12 - i22
        # (1,3)成分
        i13 = h1 - i11 - i12
        # (2,3)成分
        i23 = h2 - i21 - i22

        # (3,3)成分(2通り)
        i33 = w3 - i13 - i23
        j33 = h3 - i31 - i32

        if i31>0 and i32>0 and i13>0 and i23>0 and i33>0 and i33==j33:
          count += 1

print(count)