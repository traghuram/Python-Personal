n = 2
y = 3
prime_counter = 1

while n <= y:
    while y % n != 0:
        n += 1
        if y == n:
            prime_counter += 1
    if prime_counter == 10001:
        print (y)
        break
    n = 2
    y += 2


