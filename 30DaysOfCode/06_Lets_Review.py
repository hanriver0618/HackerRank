st=[]
num = int(input())
for i in range(num):
	st.append(str(input()))

for i in range(len(st)):
	print(st[i][::2],st[i][1::2])	
