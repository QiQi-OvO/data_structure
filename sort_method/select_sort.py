

#选择排序 从小到大  从后面找到最小值append到有序列表上
def select(disorder_list):
    min = disorder_list[0]
    n = len(disorder_list)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if min > disorder_list[j]:
                min,disorder_list[j] = disorder_list[j],min
        disorder_list[i] = min
        min = disorder_list[i+1]

#时间复杂度O(n²)


if __name__ == '__main__':
    test_list = [12,124,3,2,1]
    select(test_list)
    print(test_list)