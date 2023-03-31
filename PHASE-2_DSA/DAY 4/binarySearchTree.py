#BinarySearchTree
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def minValue(root):
    current=root
    while(current.left is not None):
        current=current.left
    return current
    
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data,end="->")
        inorder(root.right)

def insert(root,data):

    if root is None:
        return Node(data)
    elif root.data>data:
        root.left=insert(root.left,data)
    elif root.data<data:
        root.right=insert(root.right,data)
    return root

def deleteNode(root,data):
    if root is None:
        return root
    if data<root.data:
        root.left=deleteNode(root.left,data)
    elif data>root.data:
        root.right=deleteNode(root.right,data)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp

        temp=minValue(root.right)
        root.data=temp.data
        root.right=deleteNode(root.right,temp.data)
    return root
    #logic: delete node and replace it with the next-successor(right)
    #as successor is replaced now delete the succcessor present
root=Node(8)
insert(root,3)
insert(root,1)
insert(root,6)
insert(root,7)
insert(root,10)
insert(root,14)
insert(root,4)
inorder(root)
print()
deleteNode(root,8)
inorder(root)
