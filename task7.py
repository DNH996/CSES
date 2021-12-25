n = int(input().split()[0])
v,k = 0,1
while k<=n:
    if k==1: print(0)
    if k==2: print(6)
    if k>2:
        v+=k*8-16
        print(int(k*k*(k*k-1)/2-v))
    k+=1