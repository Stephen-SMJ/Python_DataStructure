class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None #头指针

    def printStack(self):
        curr = self.top
        while curr:
            print(curr.data, end=' ')
            curr = curr.next
        print()

    def push(self,data): #指针方向为新进栈的指向头节点
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        val = self.top.data
        self.top = self.top.next
        return val

    def size(self):
        count = 0
        curr = self.top
        while curr:
            curr = curr.next
            count += 1
        return count

    def isEmpty(self):
        return self.top is None


if __name__ == '__main__':
    stack1 = Stack()
    print(stack1.isEmpty())
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    stack1.printStack()
    print(stack1.pop())
    stack1.push(4)
    stack1.printStack()
    print(stack1.size())
    print(stack1.isEmpty())

