n = int(input())
if n>2 and (n%2==1 and (n/2+1/2)%2==0) or (n%2==0 and (n/2)%2==0):
    if n%2==1:
        l="1 2"
        i=3
        num = int((n+1)/2)
    else:
        l="1 4"
        i=4
        num = int(n/2)
    while i+1<=n:
        i+=1
        l+=" "+str(i)
        i+=3
        l+=" "+str(i)
    print("YES")
    print(num)
    print(l)
    if n%2==1:
        l="3"
        i=2
        num = int((n-1)/2)
    else:
        l="2 3"
        i=3
        num = int(n/2)
    while i+3<=n:
        i+=3
        l+=" "+str(i)
        i+=1
        l+=" "+str(i)
    print(num)
    print(l)
else:
    print("NO")


