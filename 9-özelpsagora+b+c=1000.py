bitti=False
for i in range(1, 1000):
    for j in range(1,1000-i):
        c = 1000-i-j
        if (c*c==i*i+j*j):
            print(i*j*c)
            bitti=True
            break
    if bitti:
        break
