class Stack: #后进先出
    def __init__(self):
        self.item = []

    def size(self):
        return len(self.item)

    def printStack(self):
        print(self.item)

    def push(self, data:int):
        self.item.append(data)

    def pop(self):
        return self.item.pop()

    def isEmpty(self):
        return self.item == []

if __name__ == '__main__':
    stack1 = Stack()
    stack1.push(0)
    stack1.push(1)
    stack1.push(2)
    stack1.printStack()
    stack1.pop()
    stack1.printStack()
    print(stack1.size())
    print(stack1.isEmpty())