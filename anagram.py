
n=int(raw_input())
L1=map(int,raw_input().split())
L2=map(int,raw_input().split())


#left triggered
ans=[]

for i in range(n-1):
    if(L1[i]+L2[i]<L1[i+1]):
        break
else:
    ans.append("LEFT")


#right triggered
for j in range(n-1,0,-1):
    if(L1[j]-L2[j]>L1[j-1]):
        break
else:
    ans.append("RIGHT")

if(len(ans)==2):
    print "BOTH"
elif(len(ans)==0):
    print "NONE"
else:
    print ans[0]


    
