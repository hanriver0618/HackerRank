num = int(input())
elements = list(map(int,input().split()))
numbers= list(map(int,input().split()))

def median_value(list):
    n = len(list)
    if n % 2 == 0:
        temp = sum(list[int(n/2-1):int(n/2+1)])/int(2)
        if temp - round(temp) ==0:
            return int(temp)
        else:
            return temp
    else:
        return list[int((n-1)/2)]

new=[]
for i in range(num):
    new+=[elements[i]]*numbers[i]

new.sort()
new_num = len(new)
q1 = median_value(new[:int(new_num/2)])
q3 = median_value(new[int((new_num-1)/2+1):])

print(round(float(q3-q1),1))
