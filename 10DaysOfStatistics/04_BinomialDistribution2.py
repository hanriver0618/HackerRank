## https://www.hackerrank.com/challenges/s10-binomial-distribution-2

i=list(map(float,input().split()))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def choose(n,p):
    return factorial(n)/(factorial(p)*factorial(n-p))

def prob(n,p,number):
    return choose(n,number)*p**number*(1-p)**(n-number)
    
p = i[0]*0.01
n = i[1]

a = prob(n,p,0)+prob(n,p,1)+prob(n,p,2)
b = 1-(prob(n,p,0)+prob(n,p,1))

print(round(a,3))
print(round(b,3))
