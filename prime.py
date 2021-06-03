
def isprime(x):
    
    if(x<2):return False
    n=2
    while n*n<=x:
        if(x%n==0):return False
        n+=1
    return True
def mirp(x):
    res=0,int(x)
    if(isprime(x)):
        while x>0:
            res+=x%10
            x=x/10
            print(x)
        return res



print(mirp(23))        





# for i in range(1,20):
#     print("{0}\t{1}".format(i,isprime(i)))

 

        
