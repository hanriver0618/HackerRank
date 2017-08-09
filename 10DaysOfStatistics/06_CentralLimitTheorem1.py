## https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1

threshold = float(input())
n = float(input())
mean = float(input())
std = float(input())

import math   
def cdf(x,mu,sigma):
    return (1/2.) * (1+math.erf((x-mu)/(sigma*2**(1/2.))))

prob = cdf(threshold,mean*n,std*n**0.5)

print(round(prob,4))
