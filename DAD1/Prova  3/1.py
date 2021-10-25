def comite(n,k):
    if k > n:
        return 0 
    elif n == k:
        return 1
    elif k == 0:
        return 1
    else:
        return comite(n-1,k) + comite(n-1,k-1)
        
print(comite(6,4))