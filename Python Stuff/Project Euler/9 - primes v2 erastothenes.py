x = 2*10**6
n = 2
i = 2
 
Comp_List = list(range(x))
Comp_List[1] = 0
while n < x:
    while i*n < x:
        Comp_List[i*n] = 0
        i += 1
        # What happens if it tries to remove an element that isn't there? What if there is no empty space once we remove it? Does the array automatically compress? - It does, damn. Need to replace elements with 0 instead of deleting them
    n += 1
    i = 2
 
print (sum(Comp_List))
