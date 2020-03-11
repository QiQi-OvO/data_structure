class TreeNode():
    def __init__(self,elem):
        self.elem = elem
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self,node = None):
        self.__father = node
    def add(self,elem):
        '''
        广度优先遍历的思想插入元素
        :param elem:
        :return:
        '''
        tmp_node = TreeNode(elem)
        if self.__father is None:
            self.__father = tmp_node
        else:
            queue_tree = [self.__father]
            while(1):
                tree_node = queue_tree.pop(0)
                if tree_node . left == None:
                    tree_node.left = tmp_node
                    break
                else:
                    queue_tree.append(tree_node.left)
                if tree_node.right == None:
                    tree_node.right =tmp_node
                    break
                else:
                    queue_tree.append(tree_node.right)
    def print_tree_info_BFS(self):
        '''
        广度优先遍历打印节点信息
        :return:
        '''
        if self.__father is None:
            print("空树")
            return
        else:
            queue_tree = [self.__father]
            while queue_tree:
                tree_node = queue_tree.pop(0)
                print(tree_node.elem,end="->")
                if tree_node.left is not None:
                    queue_tree.append(tree_node.left)
                if tree_node.right is not None:
                    queue_tree.append(tree_node.right)
        print("end")
    #深度遍历三种递归形式
    #先序遍历
    def preorder_traceback(self,root):
        if root is None:
            return
        print(root.elem,end=" ")
        self.preorder_traceback(root.left)
        self.preorder_traceback(root.right)
    #中序遍历
    def midorder_traceback(self,root):
        if root is None:
            return
        self.midorder_traceback(root.left)
        print(root.elem,end=" ")
        self.midorder_traceback(root.right)
    #后序遍历
    def postorder_traceback(self,root):
        if root is None:
            return
        self.postorder_traceback(root.left)
        self.postorder_traceback(root.right)
        print(root.elem,end=" ")

    #DFS三种模式的非递归形式
    #前序遍历 通过栈的思想来实现
    def preorder(self):
        if self.__father is None:
            print("空树")
        stack_tree = [self.__father]
        while stack_tree:
            tree_node = stack_tree.pop()
            print(tree_node.elem,end=" ")
            if tree_node.right is not None:
                stack_tree.append(tree_node.right)
            if tree_node.left is not None :
                stack_tree.append(tree_node.left)
    #中序遍历 栈
    def midorder(self):
        if self.__father is None:
            print("空树")
        stack_tree = []
        tree_node = self.__father
        while stack_tree or tree_node:
            if tree_node is not None:
                stack_tree.append(tree_node)
                tree_node = tree_node.left
            else:
                tree_node = stack_tree.pop()
                print(tree_node.elem,end=" ")
                tree_node = tree_node.right
    #后序遍历 栈
    def postorder(self):
        if self.__father is None:
            print("空树")
        stack_tree_reverse = []  #存结果的逆序
        stack_tree = [self.__father]#通过这个栈得到结果的逆序放入上述list
        tree_node = self.__father
        while stack_tree:
            tree_node = stack_tree.pop()
            if tree_node.left is not None:
                stack_tree.append(tree_node.left)
            if tree_node.right is not None:
                stack_tree.append(tree_node.right)
            stack_tree_reverse.append(tree_node)
        while stack_tree_reverse:
            print(stack_tree_reverse.pop().elem,end=' ')





if __name__ == '__main__':
    father_node = TreeNode(0)
    binary_tree = BinaryTree(father_node)
    binary_tree.add(1)
    binary_tree.add(2)
    binary_tree.add(3)
    binary_tree.add(4)
    binary_tree.add(5)
    binary_tree.add(6)
    binary_tree.add(7)
    binary_tree.add(8)
    binary_tree.add(9)
    print("广度优先遍历:")
    binary_tree.print_tree_info_BFS()
    print("前序遍历的递归模式:")
    binary_tree.preorder_traceback(binary_tree._BinaryTree__father)
    print("\n中序遍历的递归模式:")
    binary_tree.midorder_traceback(binary_tree._BinaryTree__father)
    print("\n后序遍历的递归模式:")
    binary_tree.postorder_traceback(binary_tree._BinaryTree__father)
    print("\n前序遍历的非递归模式")
    binary_tree.preorder()
    print("\n中序遍历的非递归模式")
    binary_tree.midorder()
    print("\n后序遍历的非递归模式")
    binary_tree.postorder()