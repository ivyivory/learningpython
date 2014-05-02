'''
Created on Jan 21, 2014

@author: Ivy

CC150 Chapter 2 Linked list
'''

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head  = None
        
    def printList(self):
        node=self.head
        print "[",
        while node:
            print node,
            node=node.next   
        print "]"
    
        

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)
    

def addNode(list,node):
    if list.head==None:
        list.head=node
        return
    else:
        curnode=list.head
        while curnode:
            if curnode.next:
                curnode=curnode.next
            else:
                curnode.next=node
                return
    
                
    
    
    
#2.1 remove duplicate element in linked list
def removedup(list):
    if list.head==None or list.head.next==None: return
    #fpt=Node(0)
    #spt=Node(0)
    #pt=list.head.next
    spt=list.head
    while spt:
        fpt = spt.next
        while fpt and fpt.next:
            nextnode=fpt.next
            if nextnode.data == spt.data:
                todel=fpt.next
                fpt.next = todel.next
                todel.next = None
            fpt=fpt.next
        spt=spt.next
    
                
                
def removedup2(list):
    if list.head==None or list.head.next==None: return
    Dict={}
    curnode = list.head
    i=1
    while curnode:
        nextnode = curnode.next
        if nextnode:
            if Dict.has_key(nextnode.data):
                curnode.next = nextnode.next
                nextnode.next = None 
            else:
                Dict[curnode.data]=i
                i+=1
        curnode = curnode.next
    

#2.2 find the kth to the end element 
def ktoend(list,k):
    if list.head==None or list.head.next==None: return
    spt=list.head
    fpt=list.head
    i=1
    while i<=k:
        if fpt.next:
            fpt = fpt.next
        else:
            return
        i+=1
    
    while fpt:
        if fpt.next:
            fpt=fpt.next
            spt=spt.next
        else:
            return spt
        
      
#2.3
def removethisnode(node):
    nextnode=node.next
    node.data=nextnode.data
    node.next=nextnode.next
    nextnode.next=None

#2.4 partition    
def partitionlink(list,x):
    if list.head==None or list.head.next==None: return
    listles=LinkedList()
    listmor=LinkedList()
    
    curnode=list.head
    while curnode:
        if curnode.data<x:
            newnode=Node(curnode.data)
            addNode(listles,newnode)
            end=newnode
        else:
            newnode=Node(curnode.data)
            addNode(listmor,newnode)
            
        
        curnode=curnode.next

    end.next=listmor.head
    return listles

#2.5
def addlist(p1,p2,carry):
    if list1.head==None and list2.head==None and carry==0: return None
    
    value=carry
    
    if p1:
        value += p1.data
    if p2:
        value += p2.data
    
    result = Node (value%10)
    
    if p1 and p2:
        more = addlist(None if p1==None else p1.next, None if p2==None else p2.next, 1 if value>9 else 0)
        result.next=more
    
    return result
         

#2.6
#find the first node of a loop in the linked list
def findloopnode(list):
    if list.head==None and list.head.next==None: return
    fpt=list.head
    spt=list.head
    spt=spt.next
    fpt=fpt.next.next
    
    while spt != fpt:
        if fpt.next and fpt.next.next:
            fpt=fpt.next.next
        else:
            return None
        spt=spt.next
    
    spt=list.head
    
    while spt != fpt:
        spt=spt.next
        fpt=fpt.next
    
    return spt
    

#2.7 whether a linked list is palindrome
def ispalindrome(list):
    if list.head==None:return
    stack=[]
    spt=list.head
    fpt=list.head

    while fpt and fpt.next: 
        stack.append(spt.data)
        spt=spt.next
        fpt=fpt.next.next
      
    # odd number, skip the middle
    if fpt:
        spt=spt.next
        
    while spt:
        data=stack.pop()
        if data != spt.data:
            return False
        spt=spt.next
        
    return True
    
    
    

    
#node=Node("test")
#print node

node1=Node(7)

list1=LinkedList()
list1.head=node1

node2=Node(0)
node3=Node(3)
node4=Node(9)
node5=Node(7)
node6=Node(8)
node7=Node(3)
node8=Node(5)
node9=Node(0)
nodea=Node(4)


node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6
node6.next=node7
node7.next=node8
node8.next=node9
node9.next=nodea

#addNode(list1,node2)
#addNode(list1,node3)
#list1.printList()
#print list1.head
list1.printList()
rl=partitionlink(list1,5)
rl.printList()

#list1.printList()
#removedup2(list1)
#list1.printList()

list2=LinkedList() #null list
list3=LinkedList()
list3.head=nodea # one node list

#list3.printList()
#removedup(list3)
#list3.printList()


n=ktoend(list1,3)
print n

lista=LinkedList()
listb=LinkedList()
a1=Node(7)
a2=Node(1)
a3=Node(6)
a1.next=a2
a2.next=a3
lista.head=a1
lista.printList()
b1=Node(5)
b2=Node(9)
b3=Node(2)
b1.next=b2
b2.next=b3
listb.head=b1
listb.printList()

result=addlist(lista.head,listb.head,0)
listc=LinkedList()
listc.head=result
listc.printList()

nodeA=Node("A")
nodeB=Node("B")
nodeC=Node("C")
nodeD=Node("B")
#nodeE=Node("A")

nodeA.next=nodeB
nodeB.next=nodeC
nodeC.next=nodeD
#nodeD.next=nodeE

listp=LinkedList()
listp.head=nodeB
listp.printList()
print ispalindrome(listp)
