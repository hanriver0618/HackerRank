## https://www.hackerrank.com/challenges/s10-geometric-distribution-1

ratio = list(map(float,input().split()))
n = int(input())

prob = ratio[0]/ratio[1]

answer = (1-prob)**(n-1)*(prob)

print(round(answer,3))
