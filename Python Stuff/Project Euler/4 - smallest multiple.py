y = 20
n = 20

while y<=20000000000:
    while y % n == 0:
        if n == 10:
            print (y)
            break
        n -= 1
    if n == 10:
        break
    n = 20
    y += 20
