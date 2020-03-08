class Queue():
    def __init__(self):
        self.__queue = []
    def enqueue(self,elem):
        '''
        在队列中添加一个元素
        :return:
        '''
        self.__queue.append(elem)

    def dequeue(self):
        '''
        在队列中删除一个元素
        :return:
        '''
        if self.is_empty():
            return False
        return self.__queue.pop(0)

    def is_empty(self):
        '''
        队列是否为空
        :return:
        '''
        if len(self.__queue) == 0:
            return True
        return False
    def size(self):
        '''
        返回队列的大小
        :return:
        '''
        return len(self.__queue)

    def print_queue(self):
        '''
        打印队列中的元素，从前到后
        :return:
        '''
        if self.is_empty():
            print("空队列")
            return
        for i in self.__queue:
            if i == self.__queue[-1]:
                print(i)
            else:
                print(i,end="->")

if __name__ == '__main__':
    queue = Queue()
    # print(queue.is_empty())
    # print(queue.dequeue())
    # queue.print_queue()
    # print(queue.size())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.print_queue()
    queue.dequeue()
    queue.print_queue()