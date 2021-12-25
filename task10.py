n = int(input())
i=int(n/5)
r=0
while i>0:
    r+=i
    i=int(i/5)
print(r)