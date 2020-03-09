

#Shell排序实现从小到大的排列  Shell排序本质还是插入排序通过插入排序来理解就很简单了
def shell_sort(disorder_list,gap):
    n = len(disorder_list)
    while(gap!=0):
        for i in range(gap,n):
            for j in range(i,gap-1,-gap):
                if disorder_list[j-gap] > disorder_list[j]:
                    disorder_list[j-gap],disorder_list[j] = disorder_list[j] ,disorder_list[j-gap]
        gap = gap//2

#在这里决定希尔排序的间隙
def calcu_gap(disorder_list):
    n = len(disorder_list)
    return n // 2

if __name__ == '__main__':
    test_list = [9,8,12,5,24,66,4,4,11,12,14,665,54,6126]
    shell_sort(test_list,calcu_gap(test_list))
    print(test_list)