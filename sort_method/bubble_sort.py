

#从小到大排序
def bubble(disorder_list):
    for i in range(0,len(disorder_list)-1):
        flag = 0 #这里判断有没有执行交换位置，如果没有交换位置说明已经是有序的列表了~
        for j in range(0,len(disorder_list)-i-1):
            if disorder_list[j] > disorder_list[j+1]:
                flag = 1
                disorder_list[j],disorder_list[j+1] = disorder_list[j+1],disorder_list[j]
        if flag == 0 :
            return

#时间复杂度 最优情况下O(n)
#时间复杂度 最坏情况下O(n²)

if __name__ == '__main__':
    test_list = [12,124,3,2,1]
    bubble(test_list)
    print(test_list)