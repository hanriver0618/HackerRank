phone={}
n = int(input())
for _ in range(n):
	temp = list(map(str,input().split()))
	phone[temp[0]]=temp[1]

for _ in range(n):
	key = str(input())
	value = phone.get(key, "Not found")
	if value != "Not found":
		print(key+'='+phone[key])
	else:
		print(value)

