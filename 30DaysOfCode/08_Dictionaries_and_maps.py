dic={}
for i in range(int(input())):
	temp = list(map(str,input().split()))
	dic[temp[0]]=temp[1]

answer={}
while True:
	name = str(input())
	if name == "":
		break
	else:
		phone = dic.get(name,'Not found')
		answer[name]=phone

for key, value in answer.items() :
    print(key, value)
