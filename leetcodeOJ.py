'''
Created on Nov 26, 2013

@author: Ivy
'''
result=[]
def combine(n, k):
    if n<k: 
        print "n is smaller than k"
        return
    
    #elif n==k:
        
            #for i in range(1,n): print i,","
            #print n
        #result.append(range(1,n+1))
        #return result

    if k==1:
        #for k in range(1,n+1):
            #result.append(k)
        if n > 1:
            result.append(n)
            result.append(combine(n-1,k))
            #print tempr
            #for v in tempr:
            #    result.append(v)
                    
            return    
        else:
            result.append(1)
            return 

    elif k>1:
        for i in range(n,0,-1):
            if k-1 > 0:
                #for j in range(1,n-1):
                
                #print i,","
                tempresult=combine(n-1,k-1)
                print tempresult
                #for l in range(0,len(tempresult)):
                    #result.append([n,tempresult.pop(l)])
                for v in tempresult:
                    result.append([i,v])
                    
                return result   
            #else:
                #print n,
                #for o in range(1,n+1): print o
                #tempresult2=combine(n-1,k)
                #for w in tempresult2:
                #    result.append([w])
                #return range(1,n+1)
                #return combine(n-1,k-1)


n=raw_input("enter n:")
k=raw_input("enter k:")
n=int(n)
k=int(k)
combine(n,k)
print result