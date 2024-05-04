import math
import numpy as np
import matplotlib.pyplot as plt

def ln_taylor(x, it=50):
    f = 0
    c = 1
    
    for n in range (1,it):
        #print (c,'*',x-1,'**',n,'/',math.factorial(n))
        f += (c * (x-1)**n ) / math.factorial(n)
        #print(f)
        c = (-1)**n * n*abs(c)
    return f
    
x_values = np.linspace(1, 2.05, 20)  # Example x values
y1 = [math.log(x) for x in x_values]  # Example y1 values
y2 = [ln_taylor(x,5) for x in x_values]   # Example y2 values
y3 = [ln_taylor(x,10) for x in x_values]
y4 = [ln_taylor(x,30) for x in x_values]
y5 = [ln_taylor(x,60) for x in x_values]
y6 = [ln_taylor(x,80) for x in x_values]
y7 = [ln_taylor(x,100) for x in x_values]
