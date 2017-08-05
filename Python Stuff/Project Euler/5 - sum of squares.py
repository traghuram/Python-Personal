n = 2
m = 2
z = 1
y = 1

#sum of square
while n <= 100:
    z = z + n**2
    n += 1
print (z)

# square of sum
while m <= 100:
    y = y + m
    m += 1
print (y**2)

print (y**2 - z)
