n=list(input())
l=len(n)
def ex(a,b):
    t=a
    a=b
    b=t
for i in range(int(l/2)):
    if n[i]!=n[l-1-i]:
        for j in range(i+1,l-1-i):
            if n[i]==n[j]:
                ex(n[j],n[l-i-1])
                break
        if j==l-1-i:
            print("NO SOLUTION")
            break
if(i==int(l/2)):
    print(''.join(n))
        
        


# dic={}
# dic1={}
# string=''
# le=''
# for s in n:
#     if s in dic:
#         dic[s]+=1
#     else: dic[s]=1
# for i,v in dic.items():
#     if v%2==1:
#         dic1[i]=v
#         for x in range(v):
#             le+=i
#         continue
#     for x in range(int(v/2)):
#         string+=i
# if len(dic1)>1:
#     print("NO SOLUTION")
# else:
#     t=''
#     for s in string:
#         t=s+t
#     print(string+le+t)