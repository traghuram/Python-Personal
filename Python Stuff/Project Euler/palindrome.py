n = 999
y = 999

while n>=980:
    while y>=910:
        z = n*y
        if str(z)==str(z)[::-1]:
            print (z)
            break
        y = y - 1
    y = 999
    n = n - 1

            
