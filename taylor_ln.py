import math

def ln_taylor(x, it=50):
    f = 0
    c = 1
    
    for n in range (1,it):
        #print (c,'*',x-1,'**',n,'/',math.factorial(n))
        f += (c * (x-1)**n ) / math.factorial(n)
        #print(f)
        c = (-1)**n * n*abs(c)
    return f
    
 
