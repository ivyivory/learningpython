'''
Created on Jan 15, 2014

@author: Ivy

DP
1. Coin Problem:
Given a list of N coins, their values (V1, V2, ... , VN), 
and the total sum S. Find the minimum number of coins the 
sum of which is S (we can use as many coins of one type as 
we want), or report that it's not possible to select coins 
in such a way that they sum up to S. 




'''


def coinchoice(S,N,V):
    minc=[float("inf")]*(S+1)
    #for i in range([0,S+1]):
     #   minc[i]=float("-inf")
        
    minc[0]=0
    
    for i in range(1,S+1):
        #print minc
        for j in range(0,N):
            if V[j]<=i and minc[i-V[j]]+1 < minc[i]:
                minc[i]=minc[i-V[j]]+1
                
    print minc[S]
    print minc
    return

V=[1,3,5]
S=11
N=3

coinchoice(S,N,V)




