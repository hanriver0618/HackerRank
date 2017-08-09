## https://www.hackerrank.com/challenges/s10-poisson-distribution-1

la = float(input())
n = int(input())

e=2.71828
def poisson(l,k):
    return (l**k)*e**(-l)/factorial(k)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(round(poisson(la,n),3))
