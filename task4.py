n = int(input().split()[0])
x = [int(x) for x in input().split()]
N=0
for i in range(n-1):
    if x[i]>x[i+1]:
        N+=x[i]-x[i+1]
        x[i+1]=x[i]
print(N)