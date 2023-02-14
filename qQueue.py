class Queue: #队列，先进先出
    def __init__(self):
        self.item = []

    def printQue(self):
        print(self.item)

    def enqueue(self, data):
        self.item.insert(0,data)

    def dequeue(self):
        self.item.pop()

    def size(self):
        return len(self.item)

if __name__ == '__main__':
    que = Queue()
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    que.printQue()
    que.dequeue()
    que.printQue()

