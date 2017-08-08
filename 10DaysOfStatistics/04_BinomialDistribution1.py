## https://www.hackerrank.com/challenges/s10-binomial-distribution-1

ratio = list(map(float,input().split()))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def choose(n,p):
    return factorial(n)/(factorial(p)*factorial(n-p))

p=ratio[0]/sum(ratio)
q=1-p

answer = 1-(choose(6,0)*p**0*q**6+choose(6,1)*p**1*q**5+choose(6,2)*p**2*q**4)
print(round(answer,3))
