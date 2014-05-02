'''
calculate the max value of subset of an array
2-14
Created on Jan 9, 2014

@author: Ivy

solution 3
# max subset is one of the three conditions 
# 1. A[0] itself
# 2. Start with A[0]
# 3. has nothing to do with A[0]
# therefore the max value 
   All[0] = max(A[0], Start[0], All[1]), 
   where Start[0] = A[0] + Start[1]
'''

def maxsum(A,n):
    nStart=A[n-1]
    nAll=A[n-1]
    for i in range(n-2,-1,-1):
        nStart=max(A[i],A[i]+nStart)
        nAll=max(nStart,nAll)
    
    return nAll

#solution final

def maxsumf(A,n):
    nStart=A[n-1]
    nAll=A[n-1]
    for i in range(n-2,-1,-1):
        if nStart < 0: nStart = 0 #how about all negative
        nStart += A[i]
        if nStart > nAll: nAll = nStart
        
    return nAll
        



A=[1,-2,3,5,-3,2]
B=[0,-2,3,5,-1,2]
C=[-9,-2,-3,-5,-1,-3]
M=maxsum(A,6)
N=maxsumf(B,6)
print M,N