t = int(input())
l=[]
for i in range(t):
    l.append([int(x) for x in input().split()])
for i in range(t):
    a,b=l[i][0],l[i][1]
    if (a==0 and b==0) or ((a+b)%3==0 and ((a<b and 2*a-b>=0) or (a>=b and 2*b-a>=0))):
        print("YES")
    else:
        print("NO")
        

