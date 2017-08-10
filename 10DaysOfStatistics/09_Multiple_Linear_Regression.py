## https://www.hackerrank.com/challenges/s10-multiple-linear-regression

import numpy as np
n = list(map(int,input().split()))
a = []
for i in range(n[1]):
	a.append(list(map(float,input().split())))

data_n = int(input())
b = []
for i in range(data_n):
	b.append(list(map(float,input().split())))

def create_x(data_num,feature_num,input_x):
	output_x = np.ones((data_num,feature_num+1))
	for i in range(feature_num):
		for j in range(data_num):
			output_x[j][i+1] = input_x[j][i]
	return output_x


Y = np.asarray(a)[:,n[0]]

temp_X = np.asarray(a)[:,0:n[1]]
X = create_x(n[1],n[0],temp_X)

B = np.dot(np.dot(np.linalg.inv(np.dot(X.T,X)),X.T),Y)

temp_X1 = np.asarray(b)
final_X = create_x(data_n,n[0],temp_X1)

answer = np.dot(final_X,B)

for i in range(len(answer)):
	print(round(answer[i],2))




