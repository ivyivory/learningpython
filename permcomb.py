'''
permutation and combination
Created on Jan 8, 2014

@author: Ivy
'''
import itertools
import collections

def subset(sofar, rest):
    #combination of a string
    for i in range(len(rest)):
        #print range(len(rest))
        nextone=sofar+rest[i]
        remaining=rest[i+1:len(rest)]
        subset(nextone,remaining)
    
    if len(sofar)>0:
        print sofar
        return

def combi(sofar, rest):
    #combination of a list
    for i in range(len(rest)):
        nextone = [sofar, rest[i]]
        print nextone
        remaining = rest[i+1:len(rest)]
        combi(nextone, remaining)
        
    if len(sofar) > 0:
        #output = [ x for x in sofar if x ]
        #print output
        print sofar
        return
    
        
def perm(l,k,m):
    if k==m:
        print l
        return
    else:
        for i in range(k,m+1):
            temp=l[i]
            l[i]=l[k]
            l[k]=temp
            perm(l,k+1,m)
            temp=l[i]
            l[i]=l[k]
            l[k]=temp
            
    
def permhelper(list,st,ed):
    if st == ed:
        print list
        return
    else:
        for i in range(st,ed+1):
            list[st],list[i]=list[i],list[st]
            permhelper(list,st+1,ed)
            list[st],list[i]=list[i],list[st]

def permutation(list):
    permhelper(list,0,len(list)-1)


s="abcd"
list1=[1,2,3,4]
subset("",s)
#permhelper(list1,0,len(list1)-1)
permutation(list1)
#combi([],list1)
