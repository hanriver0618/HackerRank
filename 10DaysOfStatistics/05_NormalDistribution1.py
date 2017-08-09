## https://www.hackerrank.com/challenges/s10-normal-distribution-1

x = list(map(float,input().split()))
a=float(input())
y = list(map(float,input().split()))

mean=x[0]
std=x[1]
import math

def cdf(x,mu,sigma):
    return (1/2.) * (1+math.erf((x-mu)/(sigma*2**(1/2.))))

answer1 = cdf(a,mean,std)
answer2 = cdf(y[1],mean,std)-cdf(y[0],mean,std)

print(round(answer1,3))
print(round(answer2,3))
