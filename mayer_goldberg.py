def countdig(n):
    count = 0
    while n>=1:
        count += 1
        n = n/10
    
    #print(count-1)
    return count-1

def log(m, base=10):
    a = countdig(int(m))
    r = a
    for i in range(5):
        m = (m/(base)**a)**base
        a = countdig(int(m))
        r = r + a/(10**(i+1))
    return r
   
