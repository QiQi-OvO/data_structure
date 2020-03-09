
#插入排序 从小到大   让 list[i] 一个一个插入使之成为有序表
def inset(disorder_list):
    n = len(disorder_list)
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if disorder_list[j+1] < disorder_list[j]:
                disorder_list[j+1] , disorder_list[j] =disorder_list[j] ,disorder_list[j+1]
            else:
                break

#时间复杂度最坏 O(n²)
#时间复杂度最优 O(n)

if __name__ == '__main__':
     test_list = [9,8,12,5,4]
     inset(test_list)
     print(test_list)