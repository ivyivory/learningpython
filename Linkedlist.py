'''
Created on Jan 20, 2014

@author: Ivy

class of linked list
'''

class Linkedlist:
    def __int__(self):
        self.length = 0
        self.head   = None
        
    def printBackward(self):
        print "[",
        if self.head != None:
            self.head.printBackward()
        print "]",
    
    def addFirst(self,data):
        node = Node(data)
        node.next = None
        self.head = node
        self.length = self.length + 1
        
    def addNodetoIndex(self,data,index):
        #assume head=1, insert after the index node
        if self==None: 
            print "null list"
            return
        
        node=Node(data)
        currentnode=self
        i=1
        
        while i<=index:
            if currentnode.next==None: 
                print "no such index node"
                return
            
            currentnode=currentnode.next
            i+=1
        
        node.next=currentnode.next
        currentnode.next=node
        self.length=self.length+1
        
    def addNodetoTail(self,data):
        #add node to the end of the list
        newnode=Node(data)
        newnode.next=None
        currentnode=self
        while currentnode.next :
            currentnode=currentnode.next
        
        currentnode.next=newnode
    

    def removeNode(self,index):
        #remove the index node
        if self==None: 
            print "null list"
            return
        
        i=1
        currentnode=self
        
        while i < index:
            if currentnode.next==None: 
                print "no such index node"
                return
            
            currentnode=currentnode.next
            i+=1
            
        tobedeleted=currentnode.next
        currentnode.next=tobedeleted.next
        tobedeleted.next=None



class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    
    def __str__(self):
        return str(self.data)
    
    def printBackward(self):
        if self.next != None:
            tail = self.next
            tail.printBackward()
        print self.data
        


def printList(node):
    print "[",
    while node:
        if node.next:
            print node,",",
        else:
            print node,
        node=node.next
    
    print"]"
    
def printBackward(list):
    if list==None: return
    head = list
    tail = list.next
    printBackward(tail)
    print head,
    

def removeSecond(list):
    #remove the second node
    if list==None or list.next==None: return
    first=list
    second=list.next
    first.next=second.next #make the first node refer to the third
    second.next=None #separate the second node from the rest of the list
    return second
    
def printBackwardnicely(list):
    # a wrapper for printbackward
    print "[",
    printBackward(list)
    print "]",



node=Node("test")
#print node
    
node1=Node(1)
node2=Node(2)
node3=Node(3)


node1.next=node2
node2.next=node3

#printList(node1)
#printBackward(node1)

#printList(node1)
#removed=removeSecond(node1)
#printList(removed)
#printList(node1)
printBackwardnicely(node1)