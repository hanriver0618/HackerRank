## https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient

n = int(input())
x = list(map(float,input().split()))
y = list(map(float,input().split()))

def sort_index(l):
	l_sort = l.copy() 
	number=len(l)
	for i in range(number):
		n=0
		while n < number-i:
			if l_sort[i] > l_sort[i+n]:
				l_sort[i],l_sort[i+n] = l_sort[i+n],l_sort[i]
			n+=1	
	dic = {}
	for i in range(number):
		dic[l_sort[i]]=i+1
	index=[]
	for i in range(number):
		index.append(dic[l[i]])
	return index

def spearman_rank_correlation(x,y,n):
	rank_x = sort_index(x)
	rank_y = sort_index(y)

	s=0
	for i in range(n):
		s+=(rank_x[i]-rank_y[i])**2
	
	return 1 - (6 * s) / (n * (n**2-1))

print(round(spearman_rank_correlation(x,y,n),3))
