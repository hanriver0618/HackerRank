#Write your code here
for i in range(int(input())):
    numbers = list(map(int,input().split()))
    if numbers[0] >=0 and numbers[1] >=0:
        print(numbers[0] ** numbers[1])
    else:
        print("n and p should be non-negative")
