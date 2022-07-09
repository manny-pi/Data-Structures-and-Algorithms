from lists import SinglyLinkedList, FIFO


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def compareTo(self, node):
        """ Return 1 if this node is greater than or equal to node; Return -1 otherwise """

        if self.data > node.data:
            return 1

        elif self.data < node.data:
            return -1

    def __str__(self):
        return self.data


class BinaryTree:
    def __init__(self):
        self.root = None

    def add():
        pass 
    
    def __str__(self):
        """ Print the Binary Tree using level order traversal """

        fifo = FIFO()
        fifo.add(self.root)
        result = "{"
        while not fifo.isEmpty():
            currNode = fifo.firstElement().data

            result += f"{currNode.data}: "
            if currNode.leftChild is not None:
                fifo.add(currNode.leftChild)

            if currNode.rightChild is not None:
                fifo.add(currNode.rightChild)
        
        result.replace
        result += "}"

        return result


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        """ Adds a new node N to the BST """

        if self.root is None:
            self.root = TreeNode(data)

        else:
            n = self.root
            keepGoing = True
            while keepGoing:
                if N.compareTo(n):
                    if n.leftChild is None:
                        n.leftChild = N
                        keepGoing = False
                    else:
                        n = n.leftChild

                if N.compareTo(n):
                    if n.rightChild is None:
                        n.rightChild = N
                        keepGoing = False
                    else:
                        n = n.rightChild

    def preOrder(self):
        """ Print the tree using pre-order traversal """
        pass 

    def levelOrder(self): 
        """ Print the tree using level-order traversal """
        pass 

    def inOrder(self): 
        """ Print the tree using in-order traversal """
        pass 

    def postPorder(self): 
        """ Print the tree using post-order traversal """
        pass 

    def __str__(self):
        """ Returns an in-order traversal of the BST """

        retVal = ""
        node = self.root

        return "{}"


def linkedListToBinaryTree(linkedList):
    binaryTree = BinaryTree()
    llNode = linkedList.head
    fifo = FIFO()

    while llNode is not None:
        if binaryTree.root is None:
            binaryTree.root = TreeNode(llNode.data)

        else:
            treeNode = binaryTree.root

            # Traverse the tree and find an empty child position
            while treeNode is not None:

                # Execute if empty child spot on the left
                if treeNode.leftChild is None:
                    treeNode.leftChild = TreeNode(llNode.data)
                    break

                # Execute if empty child spot on the right
                elif treeNode.rightChild is None:
                    treeNode.rightChild = TreeNode(llNode.data)
                    break

                # Execute if we need to check further down the tree
                # for an empty slot
                else:
                    fifo.add(treeNode.leftChild)
                    fifo.add(treeNode.rightChild)

                    treeNode = fifo.firstElement().data

        llNode = llNode.next

    return binaryTree


def main():

    sample_data = SinglyLinkedList()
    ls = [9, 0, 13, -1, 4, 11, 16]
    for i in ls:
        sample_data.add(i)

    result = linkedListToBinaryTree(sample_data)
    print(result)


if __name__ == "__main__": 
    main() 
