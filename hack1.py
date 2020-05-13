#prime number checker

def prime_check(n):
    for i in range(2,int(n**0.5+1)):
        if(n%i==0):
            return 'not a prime'
            break
    else:
        return n
        
for i in range(100):
    print prime_check(i)
    
