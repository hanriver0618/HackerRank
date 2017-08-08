num=int(input())
x=list(map(int,input().split()))
w=list(map(int,input().split()))

weighted_mean = sum([a*b for a,b in zip(x,w)])/sum(w)

print(round(weighted_mean,1))
