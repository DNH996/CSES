a = [int(x) for x in input().split()][0];
print(int(a));
while a!=1:
   if a % 2==0: a=a/2;
   else: a=a*3+1;
   print(int(a));

