num = int(input())
numbers = list(map(int,input().split()))

mu = sum(numbers)/num
s=0

for i in range(num):
    s+=(numbers[i]-mu)**2
print(round((s/num)**(1/2.),1))
