'''
Created on Jan 15, 2014

@author: Ivy

DP
2. Given a sequence of N numbers - A[1] , A[2] , ..., A[N]. 
Find the length of the longest non-decreasing sequence. 

'''

def leng(A,N):
    L=[0]*N
    
    for i in range(0,N):
        L[i]=1
        for j in range(0,i):
            if A[j]<=A[i] and L[j]+1>L[i]:
                L[i]=L[j]+1
                
    print L
    return
    

A=[5,3,4,8,6,7]
N=6
leng(A,N)
                
                
