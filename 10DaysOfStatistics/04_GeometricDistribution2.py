## https://www.hackerrank.com/challenges/s10-geometric-distribution-2

ratio = list(map(float,input().split()))
n = int(input())

prob = ratio[0]/ratio[1]


## first defective within nth inspection
def during(n,prob):
    for i in range(n):
        if i==0:
            s=prob
        else:
            s+=(1-prob)**i*prob
    return s

print(round(during(n,prob),3))
