a = 100

b = 200

while (a + b + (a**2 + b**2)**(1/2)) != 1000:
    while a < b:
        if (a + b + (a**2 + b**2)**(1/2)) == 1000:
            print (a, b)
        a += 1
    b += 1
    a = 100
