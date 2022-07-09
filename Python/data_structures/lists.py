class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def add(self, data):
        self.next = Node(data)

    def __str__(self):
        return str(self.data)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.__size = 0

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.add(data)

        self.__size += 1

    def size(self):
        return self.__size

    def __str__(self):
        result = "{"
        curr = self.head
        while curr is not None:
            result += str(curr)
            if curr.next is not None:
                result += ","
            else:
                result += "}"
            curr = curr.next

        return result

class FIFO(SinglyLinkedList):
    def __init__(self):
        super(FIFO, self).__init__()
        self.__size = 0

    def firstElement(self):
        if self.__size > 0:
            self.__size -= 1
            result = self.head
            self.head = self.head.next
        else:
            return None

        return result

    def add(self, data):
        self.__size += 1
        if self.head is None:
            self.head = Node(data)
            return

        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(data)

    def size(self):
        return self.__size

    def isEmpty(self):
        return self.__size == 0

def main():
    # sll = SinglyLinkedList()
    ls = [1, 2, 3, 4, 5, 6]
    # for i in ls:
    #     sll.add(i)
    # print(f"sll: {sll}\n")

    fifo = FIFO()
    for i in ls:
        fifo.add(i)
    print(f"fifo= {fifo}\n")
    print(f"fifo.size={fifo.size()}\n")
    for i in range(6):
        fifo.firstElement()
        print("Size of fifo: %i" % fifo.size())

    assert fifo.isEmpty() is True, ".isEmpty() should return 'True' "


# main()
