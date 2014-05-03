'''
Created on Nov 26, 2013

@author: Ivy
'''
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
'''


''' 2014-5-1
Pascal's Triangle
http://oj.leetcode.com/problems/pascals-triangle/'''
def generate(numRows):
    if numRows<0: return "Error"
    result=[[1]]*numRows
    templist=[1,1]
    for i in range(1,numRows+1):
        newlist = [1]*i
        if i>=3:
            for j in range(2,i):
                newlist[j-1] = templist[j-1]+templist[j-2]
            
        result[i-1] = newlist
        templist = newlist
        
    return result

#print generate(0)
#print generate(5)


'''reverse a sentence
http://oj.leetcode.com/problems/reverse-words-in-a-string/'''
def reverseString(s):
    s = list(s)
    for i in range(len(s)/2):
        s[i], s[len(s)-1-i]= s[len(s)-1-i],s[i]

    s = "".join(s)
    return s

def reverseSentence(s):
    result = ""
    s = reverseString(s)
    s = list(s)
    st = -1
    ed = -1
    for i in range(len(s)):
        if i!=len(s)-1 and s[i]==" " and s[i+1] != " ":
            st = i+1
        
        if i!=len(s)-1 and s[i]!=" " and s[i+1] == " ":
            ed = i+1
        
        if i==len(s)-1:
            if s[i]!=" " and st!=-1:
                ed = i+1
            if s[i]!=" " and st==-1:
                st = i
                ed = i+1
        
        if st!= -1 and ed != -1:
            stringlist = s[st:ed]
            string = "".join(stringlist)
            word = reverseString(string)
            result = result + word+" "
            st = -1
            ed = -1
        
    result = result[:-1]
    return result

#another way:
#return ' '.join(s.strip().split()[::-1])

#print reversehelper("abcde")
#s = " the sky   is blue "
#print reverseSentence(s)
#print ' '.join(s.strip().split()[::-1])


''' Roman to Integer
http://oj.leetcode.com/problems/roman-to-integer/ '''

def RomanToInt(s):
    roman = {'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    sub = {'I':1, 'X':10, 'C':100}

    sumint = 0
    for i in range(len(s)):
        if i!= len(s)-1 and s[i] in sub and roman[s[i+1]]>roman[s[i]]:
                sumint=sumint-roman[s[i]]
        else:
            sumint=sumint+roman[s[i]]
                
                
    return sumint

#s='MMMCMXCIX'
#print RomanToInt(s)    
 
'''Remove Element
 http://oj.leetcode.com/problems/remove-element/'''

def removeElement(A,elem):
    i=0
    j=len(A)-1
    length = len(A)
    while j>=i: #search from two ends
        if A[i]==elem: 
            if A[j]==elem:
                j=j-1
            else:
                A[i],A[j] = A[j],A[i]
                i=i+1
                j=j-1
            
            length = length -1
            
        else:
            i=i+1
                
    return A,length

#A = [0,4,4,5,4,4,0]
#elem = 4
#print removeElement(A,elem)
                


'''combination sum
http://oj.leetcode.com/problems/combination-sum/
http://leetcode.com/2010/09/print-all-combinations-of-number-as-sum.html'''

def printSum(candidates,index,n):
    result =[]
    for i in range(1,n+1):
        result.append(candidates[index[i]])
        
    print result
        
        
def combSumHelper(target,sum,candidates,sz,index,n):
    if sum > target:
        return
    if sum == target:
        printSum(candidates,index,n)
    
    for i in range(index[n],sz):
        index[n+1] = i
        combSumHelper(target,sum+candidates[i],candidates,sz,index,n+1)

    
def combinationSum(candidates,target,sz):
    index =[0]*1000
    combSumHelper(target,0,candidates,sz,index,0)
    
candidates=[2,3,6,7]
sz=4
target=7
combinationSum(candidates,target,sz)
    
            
    
    
    
    