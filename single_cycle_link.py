class Node():
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLink():
    def __init__(self, node=None):
        self.__head = node
        if node is not None:
            node.next = node

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
        if self.__head is None:
            return 0
        count = 1
        while (cursor.next != self.__head):
            count += 1
            cursor = cursor.next
        return count

    def travel(self):
        """
        遍历链表
        :return:
        """
        link = "head->"
        cursor = self.__head
        if cursor is None:
            link = "空链表"
            print(link)
            return
        link += str(cursor.elem)
        cursor = cursor.next
        while (cursor != self.__head):
            link += "->" + str(cursor.elem)
            cursor = cursor.next
        link += "->head"
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
            tmp_node.next = tmp_node
        last_node = self.__head
        while (last_node.next != self.__head):
            last_node = last_node.next
        tmp_node.next = self.__head
        self.__head =tmp_node
        last_node.next = tmp_node
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
            tmp_node.next =tmp_node
            return
        while (cursor.next != self.__head):
            cursor = cursor.next
        cursor.next = tmp_node
        tmp_node.next = self.__head
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
        if pos < 1 or pos > self.get_length() + 1:
            print("输入错误，请重试")
            return
        elif pos == 1:
            # 头插
            self.add(elem)
            return
        elif pos == self.get_length()+1:
            self.append(elem)
            return
        else:
            while (cursor is not None):
                if count == pos - 1:
                    tmp_cursor = cursor.next
                    cursor.next = tmp_node
                    tmp_node.next = tmp_cursor
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
        cursor_pre = None
        cursor = self.__head
        if self.__head == None:
            print("空链表 删除失败")
            return False
        if self.get_length() == 1:
            self.__head = None
            print("删除成功")
            return True
        last_node = self.__head
        while (last_node.next != self.__head):
            last_node =last_node.next
        while (cursor.next != self.__head):
            if cursor.elem == elem:
                if cursor == self.__head:
                    self.__head = cursor.next
                    last_node.next = self.__head
                else:
                    cursor_pre.next = cursor.next
                print("删除成功")
                return True
            cursor_pre = cursor
            cursor = cursor.next
        if cursor.elem == elem:
            cursor_pre.next = cursor.next
            print("删除成功")
            return True
        print("未发现相关元素，删除失败")
        return False

    def search(self, elem):
        """
        判断节点是否存在
        :param node:
        :return:
        """
        cursor = self.__head
        while (cursor.next != self.__head):
            if cursor.elem == elem:
                return True
            cursor = cursor.next
        if cursor.elem == elem :
            return True
        return False


if __name__ == '__main__':
    single_link = SingleLink()
    single_link.add(0)
    #print(single_link.get_length())
    single_link.travel()
    single_link.add(1)
    single_link.travel()
    single_link.add(2)
    single_link.travel()
    single_link.add(3)
    single_link.travel()
    print("链表长度"+str(single_link.get_length()))
    single_link.insert(2,4)
    single_link.travel()
    print(single_link.remove_node(0))
    single_link.travel()
    print(single_link.remove_node(1))
    single_link.travel()
    print(single_link.remove_node(3))
    single_link.travel()