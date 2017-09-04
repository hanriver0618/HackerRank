## import collections
## counts = collections.defaultdict(int)
## for _ in range(int(input())):
##    counts[input()] += 1
## for _ in range(int(input())):
##    print(counts[input()])

s=[]
for _ in range(int(input())):
    s.append(str(input()))
for _ in range(int(input())):
    print(s.count(str(input())))
