class Stack():
    def __init__(self,node = None):
        self.__stack = []

    def push(self,elem):
        '''
        压栈
        :return:
        '''
        self.__stack.append(elem)

    def pop(self):
        '''
        弹出
        :return:
        '''
        if self.is_empty() :
            return False
        return self.__stack.pop(-1)


    def peek(self):
        '''
        返回栈顶元素
        :return:
        '''
        if self.is_empty():
            return False
        return self.__stack[-1]


    def is_empty(self):
        '''
        栈是否为空
        :return:
        '''
        if len(self.__stack) == 0 :
            return True
        return False


    def size(self):
        '''
        返回栈元素个数
        :return:
        '''
        return len(self.__stack)

    def print_stack(self):
        '''
        打印栈的信息,自顶向下
        :return:
        '''
        if self.is_empty():
            print("空栈")
            return
        for i in range( len(self.__stack)-1 , -1 , -1 ):
            if i ==0:
                print(self.__stack[i])
            else:
                print(self.__stack[i], end="->")


if __name__ == '__main__':
    stack = Stack()
    stack.print_stack()

