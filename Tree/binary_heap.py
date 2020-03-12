# 堆排序和快排的选择问题:
# 因为堆排序下，数据读取的开销变大。在计算机进行运算的时候，数据不一定会从内存读取出来，而是从一种叫cache的存储单位读取。
# 原因是cache相比内存，读取速度非常快，所以cache会把一部分我们经常读取的数据暂时储存起来，以便下一次读取的时候，可以不必跑到内存去读，而是直接在cache里面找。
# 一般认为读取数据遵从两个原则：temporal locality，也就是不久前读取过的一个数据，在之后很可能还会被读取一遍；另一个叫spatial locality，也就是说读取一个数据，
# 在它周围内存地址存储的数据也很有可能被读取到。
# 因此，在读取一个单位的数据(比如1个word)之后，不光单个word会被存入cache，与之内存地址相邻的几个word，都会以一个block为单位存入cache中。另外，cache相比内存
# 小得多，当cache满了之后，会将旧的数据剔除，将新的数据覆盖上去。
# 在进行堆排序的过程中，由于我们要比较一个数组前一半和后一半的数字的大小，而当数组比较长的时候，这前一半和后一半的数据相隔比较远，
# 这就导致了经常在cache里面找不到要读取的数据，需要从内存中读出来，而当cache满了之后，以前读取的数据又要被剔除。
# 简而言之快排和堆排读取arr[i]这个元素的平均时间是不一样的。


# 采用列表的形式实现小跟堆操作,因为堆是完全二叉树，完全二叉树直接采用顺序表的结构节省内存
# 如果要对一个数组进行排序很简单就采用build heapO(n)进行建堆，然后再通过popO(logn) 得到堆元素就完成了堆排序O(nlogn)
class SmallBinaryHeap():
    __heap_list = []
    def __init__(self):
        self.__heap_list.append(0) #第一个下表不存数据 利于下标乘2 乘2+1 的特点，所以父节点从1开始

    def add(self,elem):
        '''
        新增加一个元素,新加入的节点沿着根节点上浮到相应的位置
        :return:
        '''
        self.__heap_list.append(elem)
        n = len(self.__heap_list) - 1
        while self.__heap_list[n//2] > self.__heap_list[n] and n!= 0:
            self.__heap_list[n//2],self.__heap_list[n] = self.__heap_list[n],self.__heap_list[n//2]
            n = n//2
    def print_small_heap(self):
        if len(self.__heap_list) == 1:
            print("空堆")
            return
        for i in range(1,len(self.__heap_list)):
            if i == len(self.__heap_list) - 1:
                print(self.__heap_list[i])
            else:
                print(self.__heap_list[i],end="->")

    def pop(self):
        '''
        返回出小堆顶元素,维护小根堆顺序，采用下沉的办法沿着左右节点下沉
        :return:
        '''
        if len(self.__heap_list) == 1:
            print("空堆")
            return False
        min_value = self.__heap_list[1]
        self.__heap_list[1] = self.__heap_list[len(self.__heap_list)-1] #最后节点的值赋值给 第一个节点后删除
        self.__heap_list.pop()
        #然后沿着节点进行下沉
        n = 1

        while 2*n < len(self.__heap_list):
            # 找到左右哪个节点是更小的
            if 2 * n + 1 >= len(self.__heap_list):
                min_child = 2 * n
            else:
                if self.__heap_list[2 * n] > self.__heap_list[2 * n + 1]:
                    min_child = 2 * n + 1
                else:
                    min_child = 2 * n
            if self.__heap_list[min_child] < self.__heap_list[n]:
                self.__heap_list[min_child],self.__heap_list[n] = self.__heap_list[n],self.__heap_list[min_child]
                n = min_child
            else:
                break
        return min_value

    #把一个无序表变为小根堆
    def bulid_small_binheap(self,disorder_list):
        disorder_list.insert(0,0)
        n = len(disorder_list) // 2
        #建设disorder_list是一个顺序表
        #从 最后一个叶子节点的父节点开始进行下沉操作
        while n != 0:
            #下沉操作 ↓
            tmp = n
            while 2*tmp < len(disorder_list):
                if 2*tmp + 1 > len(disorder_list)-1 :
                    min_child = 2*tmp
                else:
                    if disorder_list[2*tmp] < disorder_list[2*tmp+1]:
                        min_child = 2*tmp
                    else:
                        min_child = 2*tmp + 1
                if disorder_list[tmp] > disorder_list[min_child]:
                    disorder_list[tmp],disorder_list[min_child] =disorder_list[min_child], disorder_list[tmp]
                    tmp = min_child
                else:
                    break
            # 下沉操作 ↑
            n -= 1 #每个节点进行下沉
        self.__heap_list.clear()
        self.__heap_list = disorder_list

    def get_sort_list(self):
        n = len(self.__heap_list)
        for i in range(1,n):
            if i == n-1:
                print(self.pop())
            else:
                print(self.pop(),end="->")


if __name__ == '__main__':
    tmp_list = [12,1,5,3,4]
    small_binheap = SmallBinaryHeap()
    small_binheap.bulid_small_binheap(tmp_list)
    small_binheap.print_small_heap()
    small_binheap.get_sort_list()
    # small_binheap.add(12)
    # small_binheap.add(1)
    # small_binheap.add(5)
    # small_binheap.add(3)
    # #small_binheap.add(1)
    # small_binheap.add(4)
    # small_binheap.print_small_heap()
    # print(small_binheap.pop())
    # print(small_binheap.pop())
    # print(small_binheap.pop())
    # print(small_binheap.pop())
    # print(small_binheap.pop())
    # print(small_binheap.pop())

    pass