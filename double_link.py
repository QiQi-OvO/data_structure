class Node():
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        self.pre = None

class DoubleLink():
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """
        判断链表是否为空
        :return:
        """
        return self.__head == None

    def get_length(self):
        """
        得到链表的长度
        :return:
        """
        cursor = self.__head
        count = 0
        while (cursor is not None):
            count += 1
            cursor = cursor.next
        return count

    def travel(self):
        """
        遍历链表
        :return:
        """
        link = ""
        cursor = self.__head
        if cursor is None:
            link = "空链表"
            print(link)
            return
        link = str(cursor.elem)
        cursor = cursor.next
        while (cursor is not None):
            link += "<->" + str(cursor.elem)
            cursor = cursor.next
        print(link)
        return

    def add(self, elem):
        """
        头插
        :param Node:
        :return:
        """
        # 空

        tmp_node = Node(elem)
        if self.__head is None:
            self.__head = tmp_node
            return
        tmp_cursor = self.__head
        self.__head = tmp_node
        tmp_node.next = tmp_cursor
        tmp_cursor.pre = self.__head
        return

    def append(self, elem):
        """
        尾插
        :param Node:
        :return:
        """
        tmp_node = Node(elem)
        cursor = self.__head
        if cursor is None:
            self.__head = tmp_node
            return
        while (cursor.next is not None):
            cursor = cursor.next
        cursor.next = tmp_node
        tmp_node.pre = cursor
        return

    def insert(self, pos, elem):
        """
        指定位置插入 从1开始，指定你想插入元素的位置
        :param pos:
        :param node:
        :return:
        """
        cursor = self.__head
        tmp_node = Node(elem)
        count = 1
        if pos < 1 or pos > self.get_length()+1:
            print("输入错误，请重试")
            return
        elif pos == 1:
            # 头插
            tmp_cursor = self.__head
            self.__head = tmp_node
            tmp_node.next = tmp_cursor
            return
        elif pos == self.get_length()+1:
            self.append(elem)
            return
        while (cursor is not None):
            if count == pos - 1:
                tmp_cursor = cursor.next
                cursor.next = tmp_node
                tmp_node.pre =cursor
                tmp_node.next = tmp_cursor
                tmp_cursor.pre = tmp_node
                break
            cursor = cursor.next
            count += 1
        return

    def remove_node(self, elem):
        """
        删除节点
        :param node:
        :return:
        """
        cursor = self.__head
        if self.__head is None:
            print("空链表无法删除")
            return False
        elif self.get_length() == 1:
            self.__head = None
            print("删除成功")
            return True
        while (cursor is not None):
            if cursor.elem == elem:
                if cursor == self.__head :
                    cursor.next.pre = self.__head
                    self.__head = cursor.next
                elif cursor.next is not  None:
                    cursor.pre.next = cursor.next
                    cursor.next.pre = cursor.pre
                else:
                    cursor.pre.next = None
                print("删除成功")
                return True
            cursor = cursor.next
        print("未发现相关元素，删除失败")
        return False

    def search(self, elem):
        """
        判断节点是否存在
        :param node:
        :return:
        """
        cursor = self.__head
        while (cursor is not None):
            if cursor.elem == elem:
                return True
            cursor = cursor.next
        return False

if __name__ == '__main__':
    # a_node = Node(1)
    # b_node = Node(2)
    # a_node.next = b_node
    # b_node.pre = a_node
    double_link = DoubleLink()
    double_link.add(0)
    double_link.append(1)
    double_link.append(2)
    double_link.add(-1)
    #double_link.insert(5,0.5)
    double_link.travel()
    double_link.remove_node(0)
    double_link.travel()


