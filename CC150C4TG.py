'''
Created on Jan 28, 2014

@author: Ivy

CC150
C4:Tree and Graph
'''

class stack(object):
    def __init__(self):
        self.top=None
    
    def pop(self):
        if self.top:
            item=self.top
            self.top=self.top.next
            return item
        else:
            return None
    
    def push(self,item):
        #t=Node(item)
        item.next=self.top
        self.top=item
            
    def peek(self):
        return self.top
    
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


class TreeNode(object):
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
        


def preorder(root):
    if not root: return
    print root.data,
    preorder(root.leftchild)
    preorder(root.rightchild)
    

def inorder(root):
    if not root: return
    inorder(root.leftchild)
    print root.data,
    inorder(root.rightchild)
    

def postorder(root):
    if not root: return
    postorder(root.leftchild)
    postorder(root.rightchild)
    print root.data,
    

def iterativepreorder(node):
    stack=[]
    stack.append(node)
    while stack:
        node=stack.pop()
        if node:
            print node.data,
            stack.append(node.rightchild)
            stack.append(node.leftchild)


def iterativeinorder(node):
    stack=[]
    while stack or node:
        if node:
            stack.append(node)
            node=node.leftchild
        else:
            node=stack.pop()
            print node.data,
            node=node.rightchild
 
    
def iterativepostorder(node):
    parents = stack()
    lastnodevisited = None 
    while parents.top or node:
        if node:
            parents.push(node)
            node = node.leftchild
        else:
            peeknode = parents.peek()
            if peeknode.rightchild  and lastnodevisited != peeknode.rightchild: 
                #if right child exists AND traversing node from left child, move right
                #determine whether go up or go down
                node = peeknode.rightchild
            else:
                parents.pop() 
                print peeknode.data,
                lastnodevisited = peeknode
    

from collections import deque      
    
def levelorder(node):
    queue=deque([])
    queue.append(node)
    while queue:
        node=queue.popleft()
        print node.data,
        if node.leftchild:
            queue.append(node.leftchild)
        if node.rightchild:
            queue.append(node.rightchild)
            
        
    


root=TreeNode(1)
n2=TreeNode(2)
n3=TreeNode(3)
n4=TreeNode(4)
n5=TreeNode(5)
n6=TreeNode(6)
root.leftchild=n2
root.rightchild=n3
n2.leftchild=n4
n2.rightchild=n5
n3.rightchild=n6

#levelorder(root)

'''
preorder(root)
print("\n")
inorder(root)
print("\n")
postorder(root)    
print("\n")

iterativepreorder(root)
print("\n")
iterativeinorder(root)
print("\n")
iterativepostorder(root)        
'''

#4.1 check whether a tree is balanced (diff height<1)
import math
def checkheight(node):
    if not node: return 0
    
    leftheight=checkheight(node.leftchild)
    if leftheight==-1: return -1
    
    rightheight=checkheight(node.rightchild)
    if rightheight==-1: return -1
    
    diffheight=leftheight-rightheight
    if math.fabs(diffheight)>1:
        return -1 #not balanced
    else:
        return max(leftheight,rightheight)+1

def isBalanced(node):
    if checkheight(node)==-1:
        return False
    else:
        return True
        

#print isBalanced(root)   



#4.2 find out whether there is route between two nodes in a graph

graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}
'''
 http://www.python.org/doc/essays/graphs/
 This is a dictionary whose keys are the nodes of the graph. 
 For each key, the corresponding value is a list containing 
 the nodes that are connected by a direct arc from this node.
'''
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end: return path
    if not graph.has_key(start): return None
    
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end: return [path]
    if not graph.has_key(start): return []
    
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths 
    
    
def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end: return path
    if not graph.has_key(start): return None
    
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest



#print find_path(graph,'A','D')
#print find_all_paths(graph, 'A', 'D')
#print find_shortest_path(graph,'A','D')


#4.3 binary search tree
# given a sorted array, build a binary search tree
def buildtree(A,start,end):
    if end<start: return None
    
    mid=(start+end)/2
    
    n=TreeNode(A[mid])
    n.leftchild=buildtree(A,start,mid-1)
    n.rightchild=buildtree(A,mid+1,end)
        
    return n
    
#A=[1,2,3,4,5,6,7,8,9]
#root1=buildtree(A,0,len(A)-1)
#preorder(root1)


#4.4 linked list store each level siblings
def linkedsibilings(node):
    listoflist=[]
    current=[]
    if node: current.append(node)
    
    while current:
        listoflist.append(current)
        parents=current
        current=[]
        for parent in parents:
            if parent.leftchild:
                current.append(parent.leftchild)
            if parent.rightchild:
                current.append(parent.rightchild)
                
    return listoflist

'''
result=linkedsibilings(root)
for list in result:
    print "[",
    for element in list:
        print element.data,
    print "]" 
'''    

#4.5 check whether binary tree is a bst
def isBST(node,min,max):
    if not node: return True
    
    if (min and node.data<=min) or (max and node.data>max):
        return False
    
    if (not isBST(node.leftchild,min,node.data) or not isBST(node.rightchild,node.data,max)):
        return False
    
    return True

'''
wrong:
should smaller than all right tree, not only right child
    if node.leftchild:
        if node.data<node.leftchild.data:
            return False
        isBST(node.leftchild)
        
    if node.rightchild:
        if node.data>node.rightchild.data:
            return False
        isBST(node.rightchild)
    
    return True
'''

#print isBST(root,None,None)
#print isBST(root1,None,None)   


#4.6 find 'next' node (in-order) of any given node of a BST
# assure that each node has a link to its ancestor
'''
def findnextnode(node):
    if not node: return None
    
    parent=node.parent
    if not parent:
        if node.rightchild:
            node=node.rightchild
            while node.leftchild:
                node=node.leftchild
            return node
            
    if parent.leftchild.data==node.data:
        return parent
    else:
        while parent.parent.leftchild != parent:
            parent=parent.parent
        return parent
'''

def inorderSucc(n):
    if not n: return None
    
    if n.rightchild:
        return leftMostChild(n.rightchild)
    else:
        q=n
        x=q.parent
        while x and x.left!=q:
            q=x
            x=x.parent
        
        return x
    
def leftMostChild(n):
    if not n: return None
    
    while n.left:
        n=n.left
    
    return n


#4.7 find the first common ancestor of two nodes
'''method 1
def covers(root, p):
    if not root: return False
    if root==p: return True
    return covers(root.leftchild, p) or covers(root.rightchild,p)

def commonancester(root, p, q):
    if not root: return None
    if root==p or root==q: return root
    
    p_onleft=covers(root.leftchild,p)
    q_onleft=covers(root.leftchild,q)
    
    if p_onleft != q_onleft: return root
    
    childside = root.leftchild if p_onleft else root.rightchild
    
    return commonancester(childside, p, q) 

def commenancesterwrapper(root,p,q):
    if not covers(root,p) or not covers(root,q): return None
    return commonancester(root,p,q)
'''

#method 2

def commonAncestorHelper(root, p, q):
    if not root: return (None, False)  #treenode, boolean isAncestor
    if root==p and root==q: return (root, True)
    
    rx=commonAncestorHelper(root.leftchild, p, q)
    if rx[1]: return rx
    
    ry=commonAncestorHelper(root.rightchild,p,q)
    if ry[1]: return ry
    
    if rx[0] and ry[0]:
        return (root, True)
    elif root==p or root==q:
        isAncestor=True if rx[0] or ry[0] else False
        return (root,isAncestor)
    else:
        return (rx[0] if rx[0] else ry[0], False)
    
def commonAncestor(root, p, q):
    r=commonAncestorHelper(root,p,q)
    if r[1]: return r[0]
    return None



root=TreeNode(1)
n2=TreeNode(2)
n3=TreeNode(3)
n4=TreeNode(4)
n5=TreeNode(5)
n6=TreeNode(6)
root.leftchild=n2
root.rightchild=n3
n2.leftchild=n4
n2.rightchild=n5
n3.rightchild=n6

#levelorder(root)
#print commonAncestor(root,n2,n4).data



#4.8 whether T2 is subtree of T1 (which is a large tree)

def containsTree(t1,t2):
    if not t2: return True
    return subTree(t1,t2)

def subTree(t1,t2):
    if not t1: return False
    if t1.data==t2.data:
        if matchTree(t1,t2): return True
    return subTree(t1.leftchild,t2) or subTree(t1.rightchild,t2)

def matchTree(t1,t2):
    if not t1 and not t2: return True
    if not t1 or not t2: return False
    if t1.data != t2.data: return False
    
    return matchTree(t1.leftchild,t2.leftchild) and matchTree(t1.rightchild,t2.rightchild)

root2=TreeNode(2)
r3=TreeNode(4)
r4=TreeNode(5)
root2.leftchild=r3
root2.rightchild=r4

#print containsTree(root,root2)
    
    
#4.9 print a path starts and ends anywhere of the tree that sums up to a certain value
def findsum(node, sum, path, level):
    if not node: return
    
    path[level]=node.data
    
    t=0
    for i in range(level,-1,-1):
        t += path[i]
        if t==sum: printit(path,i,level)
        
    findsum(node.leftchild, sum, path, level+1)
    findsum(node.rightchild, sum, path, level-1)
    
    path[level]=-999
    
def findSum(node,sum):
    depth1=depth(node)
    path=[0]*depth1
    findsum(node,sum, path,0)

def printit(path, start, end):
    for i in range(start,end+1):
        print str(path[i])+" "
    print "\n"

def depth(node):
    if not node: return 0
    else:
        return 1+max(depth(node.leftchild),depth(node.rightchild))


#findSum(root,7)


#BP3-8 Maximum distance of binary tree
def GetMaximumDistance(root):
    if not root: return (0, -1)  #return MaxDistance, MaxDepth
    
    lhs = GetMaximumDistance(root.leftchild)
    rhs = GetMaximumDistance(root.rightchild)
    
    result=tuple()
    result[1] = max(lhs[1]+1, rhs[1]+1) #MaxDistance
    result[0] = max( max(lhs[0], rhs[0]), lhs[1]+rhs[1]+2 )
    return result

#BP3-9  reconstrct the tree
# given two tuple
#Preorder=('a','b','d','c','e','f')
#Inorder=('d','b','a','e','c','f')

def rebuild(Preorder, pnumber, Inorder, inumber, nTreeLen):  # use two numbers as pointer
    if not Preorder or not Inorder: return
    
    Temp = TreeNode(Preorder[pnumber])
    Root=Temp
     
    if nTreeLen == 1: return
    
    #OrgInorder=Inorder
    LeftEndnumber=inumber
    
    nTempLen=0
    
    while Preorder[pnumber] != Inorder[LeftEndnumber]:
        if not Preorder or not Inorder: return
        nTempLen+=1
        if nTempLen > nTreeLen: break
        LeftEndnumber += 1
        #LeftEnd = Inorder[LeftEndnumber]
    
    nLeftLen=LeftEndnumber-inumber #OrgInordernumber
    nRightLen= nTreeLen - nLeftLen - 1
    
    if nLeftLen>0:
        Root.leftchild=rebuild(Preorder,pnumber+1, Inorder, inumber, nLeftLen)
        
    if nRightLen >0:
        Root.rightchild=rebuild(Preorder,pnumber+nLeftLen+1,Inorder,inumber+nLeftLen+1,nRightLen)
'''
def rebuild(Preorder, Inorder, Root):
    parents=stack()
    parents.push(Preorder[0])
    lefttree=stack()
    
    node=TreeNode(Inorder[0])
    i=1
    while parents.peek() != node:
        lefttree.push(node)
        node= TreeNode(Inorder[i])
        i=i+1

def maketree(preorder, inorder):
    global tree
    if len(preorder) == 0:
        return None

    root = preorder[0]
    ind = inorder.index(root)
    linorder = filter(lambda x: inorder.index(x) ind, inorder)
    lpreorder = filter(lambda x: x in linorder, preorder)
    rpreorder = filter(lambda x: x in rinorder, preorder)
    tree[root] = [maketree(lpreorder, linorder), maketree(rpreorder, rinorder)]
    return root

tree = {}
pO = [7,10,4,3,1,2,8,11]
iO = [4,10,3,1,7,11,8,2]
maketree(pO, iO)
print tree        

MAX=256
mapIndex=[0]*MAX
def mapToIndices(inorder,n):
    for i in range(0,n):
        mapIndex[inorder[i]]=i

def buildtree(Inorder, Preorder, n, offset):
    if n==0: return
    rootVal = Preorder[0]
    i = mapIndex[rootVal] - offset
    root=TreeNode(rootVal)
    root.leftchild=buildtree(Inorder, )        
  
'''
Preorder=('a','b','d','c','e','f')
Inorder=('d','b','a','e','c','f')

pRoot=TreeNode(None)
print pRoot.data
rebuild(Preorder,0,Inorder,0,6,pRoot)
preorder(pRoot)        
     

