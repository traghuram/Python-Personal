n = 2
y = 3
prime_sum = 2

while n <= y:
    while y % n != 0:
        n += 1
        if y == n:
            prime_sum = prime_sum + n
    n = 2
    y += 2
    if y > 2*10**6:
        print (prime_sum)
        break



