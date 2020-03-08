
class DoubleQueue():
    def __init__(self):
        self.__double_queue = []
    def add_front(self,elem):
        '''
        头部添加元素
        :param elem:
        :return:
        '''
        self.__double_queue.insert(0,elem)
    def add_rear(self,elem):
        '''
        队尾添加元素
        :param elem:
        :return:
        '''
        self.__double_queue.append(elem)

    def remove_front(self):
        '''
        从头出队
        :return:
        '''
        if self.is_empty():
            print("空队列")
            return
        return self.__double_queue.pop(0)
    def remove_rear(self):
        '''
        从队尾出队
        :return:
        '''
        if self.is_empty():
            print("空队列")
            return
        return self.__double_queue.pop()

    def is_empty(self):
        '''
        双向队列是否为空
        :return:
        '''
        if len(self.__double_queue) == 0:
            return True
        return False
    def size(self):
        '''
        双向队列的大小
        :return:
        '''
        return len(self.__double_queue)

    def print_double_queue(self):
        '''
        从头到尾打印双向队列
        :return:
        '''
        if self.is_empty():
            print("空队列")
            return
        for i in self.__double_queue:
            if i == self.__double_queue[-1]:
                print(i)
            else:
                print(i,end="->")
if __name__ == '__main__':
    double_queue = DoubleQueue()
    (double_queue.remove_front())
    (double_queue.remove_front())
    double_queue.print_double_queue()
    double_queue.add_front(1)
    double_queue.add_front(0)
    double_queue.add_rear(2)
    print(double_queue.size())
    double_queue.print_double_queue()
    double_queue.remove_front()
    double_queue.print_double_queue()
    double_queue.remove_rear()
    double_queue.print_double_queue()
