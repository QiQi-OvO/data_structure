# Python数据结构学习
由于自己的基础部分薄弱，算法理解不透彻，所以寻找资料来巩固自己的基础知识，并通过Python来实现数据结构，进一步加深自己的Python基础,并把相应数据结构,实现代码放在GitHub方便以后查阅。
## 线性表
### 顺序表
    顺序表的实现方式已经被Python给封装好了，实现起来不是很有意义，所以这里只做记录，不进行实现
    同时顺序表的结构分为以下两种
#### 一体式顺序表
    表头信息和Data信息同时存在在一组内存中
    List= [n,i,data1,data2]
    其中n为分配的内存大小，或者说是Data的个数
    其中i为实际占用的多少，在上述例子中i为2
    data1，data2是存的数据
    缺点：需要存储的数据超过n后要重新销毁后重新分配新的内存空间
#### 分离式顺序表
    info_list=[n,i,index] 
    data_list= [data]
    info_list存取表头信息其中index为data_list的地址
    data_list存储数据
    优点：重新分配内存空间后，直接修改表头info_lsit的index指向新的数据地址即可,不需要修改表头地址.
    
### 链表
#### 单链表
[单链表基本功能实现](https://github.com/QiQi-OvO/data_structure/blob/master/single_link.py)
