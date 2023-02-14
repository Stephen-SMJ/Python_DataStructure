class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def addNode(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        node_list = [self.root]
        while node_list:  # 如果列表为空的话是False
            curr = node_list.pop(0)  # 递归思想，从列表中取出一个节点，查看左右指针是否有子节点，如果有的话继续查看子节点的左右指针是否有子节点
            if curr.left is None:
                curr.left = new_node
                return
            else:
                node_list.append(curr.left)
            if curr.right is None:
                curr.right = new_node
                return
            else:
                node_list.append(curr.right)

    def printTree(self):
        node_list = [self.root]
        while node_list:  # 和添加思想一样
            curr = node_list.pop(0)
            print(curr.data)
            if curr.left:
                node_list.append(curr.left)
            if curr.right:
                node_list.append(curr.right)


if __name__ == '__main__':
    tree = Tree()
    tree.addNode(1)
    tree.addNode(2)
    tree.addNode(3)
    tree.addNode(4)
    tree.addNode(5)
    tree.addNode(6)
    tree.addNode(7)
    tree.printTree()
