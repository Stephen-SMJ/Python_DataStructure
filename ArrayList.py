class ArrayList:
    #list属性：insert(index,val),append(val)#remove删值，pop删索引
    def __init__(self, capacity:int = 10): #python形参指定变量类型和初始化值的语法： (variable:type=default)
        #_开头为私有变量
        self.data = []
        self._capacity = capacity

    def __len__(self) -> int: #->为函数添加元数据,描述函数的返回类型，从而方便开发人员使用。
        return len(self.data)

    def __iter__(self): #迭代
        for item in self.data:
            yield item

    def __repr__(self): #用字符串表示
        return str(self.data)

    #insert对应pop, append对应remove
    def insert(self, index:int, value:int): #插入
        if index < 0 or len(self) >= self._capacity: #index小于0或数组长度大于等于容量时无法插入
            return False
        else:
            self.data.insert(index, value)
            return True

    def deleteByIndex(self, index:int):
        if index < 0 or index >= len(self): #小于0或索引大于列表长度 index最大为长度-1
            return False
        else:
            self.data.pop(index)
            return True

    def deletByValue(self,val:int):
        if val not in self.data:
            return False
        else:
            self.data.remove(val)
            return True

    def findByIndex(self, index:int):
        if index <0 or index > len(self.data):
            return False
        else:
            return self.data[index]

    def findByValue(self, value:int):
        if value not in self.data:
            return False
        else:
            return self.data.index(value)


if __name__ == '__main__':
    #初始化：
    array = ArrayList(5)
    print(type(array))
    #赋值：
    #array._data = [4, 5, 3, 10, 9]
    array.insert(0, 3)
    array.insert(0, 4)
    array.insert(1, 5)
    array.insert(3, 9)
    array.insert(3, 10)
    print(array)
    print(array.insert(0, 100)) #assert在表达式条件为 false 的时候触发异常
    print(array.__len__())
    print(array.findByIndex(0))
    print(array.findByValue(10))
    print(array.deletByValue(4))
    print(array.deleteByIndex(0))
    print(array)
    # assert array.delete(4) is True
    # print(array)
    # array.insert(3, 7)
    # print(array)


