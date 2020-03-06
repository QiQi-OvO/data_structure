class Node():
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLink():
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
            link += "->" + str(cursor.elem)
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
        tmp_cursor = self.__head
        self.__head = tmp_node
        tmp_node.next = tmp_cursor
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
        return

    def insert(self, pos, elem):
        """
        指定位置插入
        :param pos:
        :param node:
        :return:
        """
        cursor = self.__head
        tmp_node = Node(elem)
        count = 1
        if pos < 1 or pos > self.get_length():
            print("输入错误，请重试")
            return
        elif pos == 1:
            # 头插
            tmp_cursor = self.__head
            self.__head = tmp_node
            tmp_node.next = tmp_cursor
            return
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
        cursor = self.__head
        while (cursor.next is not None):
            if cursor.next.elem == elem:
                cursor.next = cursor.next.next
                print("删除成功")
                return
            cursor = cursor.next
        print("未发现相关元素，删除失败")
        return

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
    single_link = SingleLink()
    single_link.append("第2个元素")
    single_link.append("第4个元素")
    single_link.add("第1个元素")
    single_link.insert(3, "第3个元素")
    # single_link.remove_node("第3个元素")
    print("链表长度" + str(single_link.get_length()))
    print("链表:")
    single_link.travel()
    print("第4个元素是否存在:")
    print(single_link.search("第4个元素"))
    print("第5个元素是否存在:")
    print(single_link.search("第5个元素"))
