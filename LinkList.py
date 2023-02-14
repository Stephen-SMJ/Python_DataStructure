class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None #此时的head是个指针而不是节点

    def __len__(self): #长度
        curr = self.head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        return count

    def printList(self): #打印链表
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=' ')
            curr_node = curr_node.next
        print()

    def appendNode(self, data): #在最后添加节点
        new_node = Node(data)  #初始化一个新节点
        if self.head is None:  #如果list为空则为头节点
            self.head = new_node
            return
        last_node = self.head #指针从头开始
        while last_node.next: #遍历
            last_node = last_node.next
        last_node.next = new_node #在结尾添加

    def prepend(self, data): #在最前面添加
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node #重新赋值，把指针变节点

    # def insert(self, pre_node: Node, data): #在某个节点后面插入一个节点
    #     if not pre_node:
    #         print("previous node is not in list")
    #         return
    #     new_node = Node(data)
    #     new_node.next = pre_node.next #顺序：先指向prenode的下一个节点，在断开prenode的指向（顺序不能反）
    #     pre_node.next = new_node

    def insert(self, index, data): #在index之后插入,index从0开始
        if index <= 0:
            self.prepend(data)
        elif index >= self.__len__():
            self.appendNode(data)
        else:
            new_node = Node(data)
            pre_node = self.head
            count = 0
            while count < index-1:  #while循环先+1再进下一次判断，所以要-1
                pre_node = pre_node.next
                count += 1
            new_node.next = pre_node.next
            pre_node.next = new_node


    def delete(self,data): #删除
        curr_node = self.head
        pre_node = None
        while curr_node and curr_node.data != data: #遍历，需要同时遍历出前节点和现节点
            pre_node = curr_node
            curr_node = curr_node.next
        if curr_node is None: #遍历结束，如果没有key则返回
            return
        pre_node.next = curr_node.next #删除
        curr_node = None

    def find(self, data): #查找
        curr = self.head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False

if __name__ == '__main__':
    link = LinkList()
    link.appendNode(1)
    link.appendNode(2)
    link.prepend(5)
    link.printList()
    print("length:",link.__len__())
    link.insert(2,15)
    link.printList()
    link.delete(15)
    link.printList()
    print(link.find(11))


