'''
Created on Jan 19, 2014

@author: Ivy

review all the sort methods
'''
import collections

#select sort O(n^2)
def selsort(L):
    for i in range (0,len(L)):
        minv=float("inf")
        k=0 #location
        for j in range(i,len(L)):
            if L[j]<=minv:
                minv=L[j]
                k=j
        temp=L[k]
        L[k]=L[i]
        L[i]=temp
      
    return L

#insert sort O(n^2)
def inssort(L):
    k=0
    for i in range (k+1,len(L)):
        for j in range(0,k+1):
            if L[i]>L[j]:
                j=j+1
            else:
                for m in range(k+1,j,-1):
                    L[m]=L[m-1]
                L[j]=L[i]
    
    return L

def inssort2(L):
    for i in range(len(L)):
        for j in range(i,0,-1):
            if L[j]>L[i]:
                temp = L[i]
                L[i]=L[j]
                L[j]=temp
                
    return L
        
#merge sort O(nlogn)
def mergesort(L):
    #if len(L)<=1:
    #   return L
    #python will error as no len method for int, therefore need to determine
    #whether it's one-element int or list using isinstance collections.Iterable
    if isinstance(L,collections.Iterable):   
        return L
    elif len(L)<=1:
        return L
    
    #middle=len(L)/2
    Left=L[0:len(L)/2]
    Right=L[len(L)/2+1]
    Left=mergesort(Left)
    Right=mergesort(Right)
    
    return merge(Left,Right)

def merge(a,b):
    i=0
    j=0
    k=0
    R=[0]*(len(a)+len(b))

    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            R[k]=a[i]
            k=k+1
            i=i+1
        else:
            R[k]=b[j]
            k=k+1
            j=j+1
    
    print i,j
            
    if i<len(a):
        for m in range(i,len(a)):
            R[k]=a[m]
            k=k+1
    elif j<len(b):
        for m in range(j,len(b)):
            R[k]=b[m]
            k=k+1
    return R
    
#bubble sort--change sort O(n^2)
def bubsort(L):
    flag=True
    while flag:
        flag=False
        for i in range(len(L)-1):
            if L[i+1]<L[i]:
                temp=L[i]
                L[i]=L[i+1]
                L[i+1]=temp
                flag=True
                
    return L

#quicksort 
def quicksort(L):
    if isinstance(L,collections.Iterable):   
        return L
    elif len(L)<=1:
        return L
    
    Less=[]
    More=[]
    pivot=L[len(L)-1]
    for i in range(len(L)):
        if L[i]<pivot:
            Less.append(L[i])
        else:
            More.append(L[i])

    return [quicksort(Less),quicksort(More)]

def heapsort(L,length):
    heapify(L,length)
    end=length-1
    # The following loop maintains the invariants that a[0:end] is a heap and every element
    #beyond end is greater than everything before it (so a[end:count] is in sorted order).
    while end>0:
        L[end],L[0]=L[0],L[end]
        end=end-1
        siftdown(L,0,end)
    
# Put elements of a in heap order, in-place 
def heapify(L,length):
    #start is assigned the index in  of the last parent node
    start=(length-2)/2
    while start>=0:
        #sift down the node at index start to the proper place such that all nodes below
        #the start index are in heap order
        siftdown(L,start,length-1)
        start=start-1
        #after sifting down the root all nodes/elements are in heap order

def siftdown(L,start,end):
    root=start
    while root*2+1<=end:  #While the root has at least one child
        child=root*2+1    #left child
        swap=root         #keeps track of child to swap with 
        
        if L[swap]<L[child]:
            swap=child
        if child+1 <= end and L[swap]<L[child+1]:
            swap=child+1
        if swap<>root:
            L[root],L[swap]=L[swap],L[root]
            root=swap     #repeat to continue sifting down the child now
        else:
            return

 
#heap sort from wikipedia
def heap_sort(lst):
    for start in range((len(lst)-2)/2,-1,-1):
        sift_down(lst,start,len(lst)-1)
 
    for end in range(len(lst)-1,0,-1):
        lst[0],lst[end] = lst[end],lst[0]
        sift_down(lst,0,end-1)
    return lst
 
def sift_down(lst,start,end):
    root = start
    while True:
        child = 2*root + 1
        if child > end:break
        if child+1 <= end and lst[child] < lst[child+1]:
            child += 1
        if lst[root] < lst[child]:
            lst[root],lst[child] = lst[child],lst[root]
            root = child
        else:
            break


L=[9,2,1,7,6,8,5,3,4]
L1=selsort(L)
L2=inssort2(L)
L3=mergesort(L)
L4=bubsort(L)
L5=quicksort(L)
L6=heap_sort(L)
heapsort(L,9)
print L
