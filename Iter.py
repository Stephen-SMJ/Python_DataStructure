'''
python中的迭代器和生成器：
    迭代器对象 ---实现了迭代器协议的对象；可遍历的对象，如list
    迭代器协议----
'''

# 首先创建一个类，实例化一个普通的对象。

class Dogs(object):
    def __init__(self, nums):  # 我家有nums条狗
        self.nums = nums
        self.start = -1

    def __iter__(self):  # 通过实现__iter__方法，则对象就成了迭代对象
        return self

    def __next__(self):  # 实现next方法，即迭代器协议;每一次for循环都调用该方法
        self.start += 1
        if self.start >= self.nums:  # 若超出，则停止迭代
            raise StopIteration()
        return self.start

def foo(num):
    print("starting...")
    while num < 10:
        num = num+1
        yield num

if __name__ == '__main__':
    # dogs = Dogs(10)
    # print(dir(dogs))  # 返回该对象所拥有的方法和属性名
    # for dog in dogs:
    #     print(dog)

    for n in foo(0):
        print(n)
