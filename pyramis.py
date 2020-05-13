t=int(raw_input())
for i in range(t):
    n=int(raw_input())
    L=[]
    M=[]
    for k in range(1,n+1):
        L.append(k)
    ori=L[:]
    N=0
    serv=n
    ans=0
    while N<n:
        counted=0
        for j in ori:
            if (serv%j==0):
                N+=1
                if(counted==0):
                    ans+=1
                    counted=1
                L.remove(j)
        serv+=1
        ori=L[:]
    ans=n-ans

    if(n<6):
        print ans
    elif(n<10):
        print ans-1
    elif(n<20):
        print ans-2
                
                
                
        
