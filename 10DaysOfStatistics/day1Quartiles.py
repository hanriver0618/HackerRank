num = int(input())
numbers = list(map(int,input().split()))
numbers.sort()

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

print(median_value(numbers[:int(num/2)]))
print(median_value(numbers))
print(median_value(numbers[int((num-1)/2+1):]))

