# Problem 1
def approximate_pi(m):
    sum = 0
    n = 0
    while n < m + 1:
        term = ((-1) ** n)/ ((2 * n) + 1)
        sum = sum + term
        n += 1
    return sum
   
print(approximate_pi(0, 1000000000))


m =1000
sum = 0
for i in range(m +1):
    sum += ((-1) ** i) / ((2 * i) + 1)
print(sum)

# Problem 2
def simplify_fraction(n,m):
    if n > m:
        i = m
        while m > 0:
            if (n % i == 0) and (m % i == 0):
                print((n/i), "/",(m/i))
                return
            else:
                i-=1
    if n < m:
        i = n
        while n > 0:
            if (n % i == 0) and (m % i == 0):
                print((n/i), "/",(m/i))
                return 
            else:
                i-=1
    else:
        print(1)

simplify_fraction(4,20)    
    
    
#Problem 3

print(math.pi)


import math
   
def pi_sig_figs(n):
    pi = 0
    i = 0
    while int((math.pi) *(10 ** n)) != int(4 * pi *(10**n)):
        pi += ((-1) ** i)/((2*i) +1)
        i += 1
    print("To get pi to n sig figs, use ", i + 1, "terms")

pi_sig_figs(3)

    
    
#Problem 4a
def signature_next_day(y, m, d):
    #check for leap years
  
    if (y % 4 == 0) and (y % 400 == 0) and (m == 2) and (d == 28): 
        print(y,"/",m,"/",d+1)
    if (y % 4 == 0) and (y % 400 == 0) and (m == 2) and (d == 29):
        print(y,"/", m +1, 1)
    if (y % 4 == 0) and (y % 100 != 0):
        if (m == 2) and (d== 28):
            print(y,"/", m,"/", d +1)
        if (m == 2) and (d== 29):
            print(y,"/", m + 1,"/", 1)
    
    #last day of the year
    if m == 12: 
        if d == 31:
            print (y+1,"/", 1,"/",1)
        else:
            print (y,"/",m,"/",d+1)
            
    #check for last day of month
    if m == 1 or 3 or 5 or 7 or 8 or 10:
        if d == 31:
             print (y,"/", m +1,"/",1)
        else:
            print (y,"/",m,"/",d+1)
    if m == 2:
        if d == 28:
            print(y,"/", m +1,"/",1)
        else:
            print (y,"/",m,"/",d+1)
    
    if m == 4 or 6 or 9 or 11:
        if d == 30:
            print(y,"/", m +1,"/",1)
        else:
            print (y,"/",m,"/",d+1)
    
    
signature_next_day(1700, 5, 5)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    








