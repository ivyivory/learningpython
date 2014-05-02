'''
Created on Jan 8, 2014

@author: Ivy
'''

def bisearch(l,st,ed):
    if ed-st<=1:
        if l[st]<l[ed]:
            max=l[ed]
            min=l[st]
            return [max,min]
        else:
            max=l[st]
            min=l[ed]
            return [max,min]

    [maxL,minL]=bisearch(l,st,st+(ed-st)/2)
    [maxR,minR]=bisearch(l,st+(ed-st)/2+1,ed)
    if maxL>maxR:
        max=maxL
    else:
        max=maxR
        
    if minL<minR:
        min=minL
    else:
        min=minR
        
    return [max,min]


l=[5,6,8,3,7,9]
[max,min]=bisearch(l,0,len(l)-1)
print max,min
