i1 = list(map(float,input().split()))
i2 = list(map(float,input().split()))
i3 = list(map(float,input().split()))
i4 = list(map(float,input().split()))
i5 = list(map(float,input().split()))

x = [i1[0],i2[0],i3[0],i4[0],i5[0]]
y = [i1[1],i2[1],i3[1],i4[1],i5[1]]

def get_b(x,y):
	n=len(x)
	xy = [a*b for a,b in zip(x,y)]
	x_sq = sum([i**2 for i in x])
	return (n*sum(xy)-sum(x)*sum(y)) / (n*x_sq - sum(x)**2)

def get_a(x,y):
	n=len(x)
	mu_x = sum(x)/n
	mu_y = sum(y)/n
	return mu_y - get_b(x,y) * mu_x

input = 80
print(round(get_a(x,y) + get_b(x,y) * input, 3))
