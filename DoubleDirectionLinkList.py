class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkList():
    def __init__(self):
        self.head = None

    def size(self):
        count = 0
        curr = self.head
        while curr:
            curr = curr.next
            count += 1
        return count

    def printLink(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def append(self, data): #尾部添加
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            curr = self.head  #先找到尾节点
            while curr.next:  #如果循环中要给curr.next赋值那么循环条件要为curr.next, 否则要为curr
                curr = curr.next
            curr.next = node
            node.prev = curr


    def prepend(self, data): #在头部添加
        node = Node(data)
        self.head.prev = node
        node.next = self.head
        self.head = node

    def insert(self, index, data): #在index后插入，从0开始
        if index <= 0:
            self.prepend(data)
        elif index >= self.size()-1:
            self.append(data)
        else:
            node = Node(data)
            curr = self.head
            count = 0
            while count < index-1: #插入时，指针要指到index的前一个位置
                curr = curr.next
                count += 1

            node.next = curr.next
            node.prev = curr
            curr.next.pre = node
            curr.next = node

    def delete(self, data):
        curr = self.head
        if curr.data == data:
            self.head = curr.next
            curr.next.pre = None
        else:
            while curr.next.data != data: #找到删除节点的前一个节点
                curr = curr.next
            if curr.next is not None:
                curr.next.prev = curr
            curr.next = curr.next.next

    def find(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False

if __name__ == '__main__':
    linklist = DoubleLinkList()
    linklist.append(1)
    linklist.append(2)
    linklist.append(3)
    linklist.append(4)
    linklist.append(5)
    linklist.prepend(0)
    linklist.printLink()
    print(linklist.find(5))
    print("size为：",linklist.size())
    linklist.insert(4,7)
    linklist.printLink()
    linklist.delete(7)
    linklist.printLink()







