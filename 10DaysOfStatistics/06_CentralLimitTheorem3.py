## https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3

n=int(input())
mean=float(input())
std=float(input())
percentile=float(input())
z_value=float(input())

mu = mean
sigma = std / n**(0.5)

x = z_value * sigma + mu

b = x
a = 2 * mu - b

print(round(a,2))
print(round(b,2))

