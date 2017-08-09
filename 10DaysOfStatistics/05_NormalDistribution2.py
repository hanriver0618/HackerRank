## https://www.hackerrank.com/challenges/s10-normal-distribution-2
x = list(map(float,input().split()))
a = float(input())
b = float(input())

mean = x[0]
std = x[1]

import math
def cdf(x,mu,sigma):
    return (1/2.) * (1+math.erf((x-mu)/(sigma*2**(1/2.))))

answer1 = 1 - cdf(a,mean,std)
answer2 = 1 - cdf(b,mean,std)
answer3 = cdf(b,mean,std)

print(round(answer1 * 100, 2))
print(round(answer2 * 100, 2))
print(round(answer3 * 100 ,2))
