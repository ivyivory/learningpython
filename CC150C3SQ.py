'''
Created on Jan 23, 2014

@author: Ivy

CC150 Chapter 3 
Stacks and Queues
'''


class stack(object):
    def __init__(self):
        self.top=None
    
    def pop(self):
        if self.top:
            item=self.top.data
            self.top=self.top.next
            return item
        else:
            return None
    
    def push(self,item):
        t=Node(item)
        t.next=self.top
        self.top=t
            
    def peek(self):
        return self.top.data
    
    def printstack(self):
        node=self.top
        print "[",
        while node:
            print node.data,
            node=node.next
        print "]"
    

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
    def __str__(self):
        return str(self.data)


#3.1 one array three stack
#3.2 add min function
class stackwithmin(stack):
    def __init__(self):
        super(stackwithmin,self).__init__()
        self.minstack=stack()
    
    def push(self,value):
        if value < self.minvalue():
            self.minstack.push(value)
            
        super(stackwithmin,self).push(value)
        
    def pop(self):
        value=super(stackwithmin,self).pop()
        if value==self.minvalue():
            self.minstack.pop()
        return value
    
    def minvalue(self):
        if not self.minstack.top:
            return float("inf")
        else:
            return self.minstack.peek()
'''

s1=stackwithmin()

s1.push(5)
s1.push(6)
s1.push(3)
s1.push(7)

s1.printstack()
print s1.minvalue()

s1.pop()
s1.printstack()
print s1.minvalue()

s1.pop()
s1.printstack()
print s1.minvalue()

''' 
    
#3.3 SetOfStack
'''
Threshold=3

class SetOfStack():
    def __init__(self):
        self.top=None
        self.total=0    #total number of stacks
        self.layer=0 #current "layer" in stack if arrive threshold, build a new one
    
    def pop(self):
        if self.top==None:
            return None
        
        if self.top.next:
            topnode=self.top
            self.top=topnode.next
        return topnode
    
    def push(self,data):
        newnode=Node(data)
        if self.total==0:  #first node
            newnode.next=self.top
            self.top=newnode
            self.layer += 1
            
        elif self.total>0:
            if self.layer<Threshold:  #not reach threshold
                newnode.next=self.top
                self.top=newnode
                self.layer += 1
            elif self.layer==Threshold: #start new stack
                self.total += 1
                self.layer = 0
                self.top=newnode
             
            
class SetStack():
    def __init__(self):
        self.stacks=[]
        self.capacity=3
    
    def getLastStack(self):
        if len(self.stacks) == 0: return None
        return self.stacks[len(self.stacks)-1]
    
    def push(self,data):
        last = self.getLastStack()
        if last and self.layer < self.capacity:
            last.push(data)
        else:
            newstack=stack()
            newstack.push(data)
            self.stacks.append(newstack)
    
    def pop(self):
        last=self.getLastStack()
        v = last.pop()
        if not last.top:
            self.stacks.pop()
        return v
    
    def isEmpty(self):
        last=self.getLastStack()
        return last==None
    
    def popAt(self,index):
        return self.leftshift(index,True)
    
    def leftshift(self,index,removeTop):
        ss= self.stacks[index]
        
'''
        
            

#3.4 Hanoi

class Tower():
    def __init__(self,i):
        self.disks=stack()
        self.index = i
    
    def add(self,d):
        if self.disks.top and self.disks.peek()<=d:
            print "Error placing disk %d" % d
        else:
            self.disks.push(d)
        
    def moveTopto(self,t):
        top = self.disks.pop()
        t.add(top)
        print("Move disk "+str(top)+" from "+str(self.index)+" to "+str(t.index))
        
    def moveDisks(self, n, destination, buffer):
        if n >0:
            self.moveDisks(n-1, buffer, destination)
            self.moveTopto(destination)
            buffer.moveDisks(n-1,destination,self)


'''
n=5

towers=[Tower(0),Tower(1),Tower(2)]
#for i in range(3):
#    towers[i]=Tower(i)

for i in range(n-1,-1,-1):
    towers[0].add(i)

towers[0].moveDisks(n,towers[2],towers[1])
 

'''


class queue(object):
    def __init__(self):
        self.first=None
        self.last=None
        
    def enqueue(self,data):
        newnode=Node(data)
        if not self.first:  #null queque, first node
            self.first=newnode
            self.last=newnode
        else:
            newnode.next=self.last
            self.last=newnode
    
    def dequeue(self):
        if self.first:
            value=self.first.data
            self.first=self.first.next
            return value
        else:
            return None
    
    def peek(self):
        return self.first.data
            
    def printqueue(self):
        node=self.first
        print "[",
        while node:
            print node.data,
            node=node.next
        print "]"
        
    
#3.5 use two stack for queue

class MyQueue():
    def __init__(self):
        self.newstack=stack()
        self.oldstack=stack()
    
    def add(self,value):
        self.newstack.push(value)
    
    def shiftstack(self):
        if not self.oldstack.top:
            while self.newstack.top:
                self.oldstack.push(self.newstack.pop())
    
    def peek(self):
        self.shiftstack()
        return self.oldstack.peek()
                
    def remove(self):
        self.shiftstack()
        return self.oldstack.pop()

'''
class MyQueue():
    def __init__(self):
        self.s1=stack()   #enter here
        self.s2=stack()   #leave here
        
    def enqueue(self,data):
        self.s1.push(data)
        
    def dequeue(self):
        if self.s2.top:
            return self.s2.pop()
        else:
            while self.s1.top:
                self.s2.push(self.s1.pop())
                
            return self.s2.pop()
    

q=MyQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.s1.printstack()
q.s2.printstack()

q.dequeue()
q.enqueue(4)
q.s1.printstack()
q.s2.printstack()

q.dequeue()

q.s1.printstack()
q.s2.printstack()
'''
        

#3.6 sort a stack
def sortstack(s):
    r=stack()
    while s.top:
        current=s.pop()
        while r.top and r.peek() > current:
            s.push(r.pop())
        
        r.push(current)
    
    return r



#3.7 Adoption Center
#from collections import deque

class Animal(object):
    def __init__(self,name):
        self.name=name
    
    def setorder(self,order):
        self.order=order
    
    def getorder(self):
        return self.order
    
class Dog(Animal):
    def __init__(self,name):
        super(Dog,self).__init__(name)

class Cat(Animal):
    def __init__(self,name):
        super(Cat,self).__init__(name)

    
class AnimalQueue():
    def __init__(self):
        self.Dogs=queue()
        self.Cats=queue()
        self.order=0
        
    def enqueue(self,a):
        a.setorder(self.order)
        self.order +=1
        if isinstance(a,Dog):
            self.Dogs.enqueue(a)
        elif isinstance(a,Cat):
            self.Cats.enqueue(a)
        
    def dequeue(self):
        if not self.Dogs.first:
            return self.dequeueCats()
        elif not self.Cats.first:
            return self.dequeueDogs()
        
        dog=self.Dogs.peek()
        cat=self.Cats.peek()
        
        if dog.order<cat.order:
            return self.dequeueDogs()
        else:
            return self.dequeueCats()
        
    def dequeueDogs(self):
        return self.Dogs.dequeue()
    
    def dequeueCats(self):
        return self.Cats.dequeue()
    

A=Cat("A")
B=Dog("B")
C=Dog("C")
D=Cat("D")
E=Cat("E")
L=AnimalQueue()
L.enqueue(A)
L.enqueue(B)
L.enqueue(C)
L.enqueue(D)
L.enqueue(E)

L.Cats.printqueue()
L.Dogs.printqueue()
    
L.dequeue()
#L.dequeue()
    
L.Cats.printqueue()
L.Dogs.printqueue()
       
        
        
        
    
    
    




             
'''
using lists
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
'''