## https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient

n = int(input())
x = list(map(float,input().split()))
y = list(map(float,input().split()))


def pearson_correlation(list_x,list_y,n):
	mu_x = sum(list_x) / n
	mu_y = sum(list_y) / n

	sigma_x = (sum((x1-mu_x)**2 for x1 in list_x) / n) ** 0.5
	sigma_y = (sum((y1-mu_y)**2 for y1 in list_y) / n) ** 0.5

	s=0.
	for i in range(n):
		s += (list_x[i]-mu_x) * (list_y[i]-mu_y)
	return s / (n * sigma_x * sigma_y)

print(pearson_correlation(x,y,n))

