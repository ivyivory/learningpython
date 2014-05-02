'''
Created on Nov 24, 2013

@author: Ivy
'''
#design an algorithm to determine whether a string has all the unique characters
#suppose it's in ASCII


def unique (string):
    for i in range(0,len(string)):
        #print "i:",string[i]
        for j in range(i+1,len(string)):
            #print "j:",string[j]
            if string[i]==string[j]:
                print "not unique"
                return False
            
    print "unique"
    return True

string=raw_input("enter here:")
#print len(string)
unique(string)
'''

'''
#hashtable
def unique(string):
    dict={}
    for cha in string:
        if cha in dict.keys():
            print "not unique"
            return False
        else:
            dict[cha]=1 
    
    print"unique"
    return True
    
string=raw_input("enter here:")
unique(string)      


#self-defined hashtable
class KeyValue:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        
class HashTable:
    def __init__(self):
        self.list=[0,0,0,0,0,0,0,0,0,0]  # self.list=[0]*10 will also work 
    def get(self,key):
            # call self.hash(key) to get index
            # find the correct key at that bucket
        
    def set(self,key,value):
            # call self.hash(key) to get index
            # insert new key-value pair to that bucket.
        

    def hash(self,key):
            # see above explanation of a hash function.


#1.2 reverse string
def reverse(s):
    #for i in range(0,len(s)/2):
    #    temp=s[i]
    #    s[i]=s[len(s)-1-i] #'str' object does not support item assignment
    #    s[len(s)-i]=temp
    news=[]
    for i in range(0,len(s)):
        news.append(s[len(s)-1-i])
        
    news=''.join(news)  #join list that contains string into one long string
    return news

s=raw_input("string to reverse:")
print reverse(s)
'''

#1.3 
def permute(s1,s2):
        
