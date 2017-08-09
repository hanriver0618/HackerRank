## https://www.hackerrank.com/challenges/s10-poisson-distribution-2

x= list(map(float,input().split()))

a = 160 + 40 * (x[0]+x[0]**2)
b = 128 + 40 * (x[1]+x[1]**2)

print(round(a,3))
print(round(b,3))

