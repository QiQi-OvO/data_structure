

#快速排序，从小到大
#最好情况O（nlogn） 最坏情况O(n²)
def quick_sort(disorder_list,first,last):
    if first >= last:
        return
    low = first
    high = last
    mid_value = disorder_list[first]
    while low != high:
        #高位指针往前走,直到  low 跟 high 重合 或者 high指向的值小于mid value
        while low<high and disorder_list[high] >= mid_value:
            high -= 1
        disorder_list[low] = disorder_list[high]
        #然后把高位的值，放入低位，低位指针进行寻找，直到low = high 或者 low的指向大于 mid value
        while low < high and disorder_list[low] < mid_value:
            low += 1
        disorder_list[high] = disorder_list[low]
    disorder_list[low] = mid_value
    quick_sort(disorder_list,first,low-1)
    quick_sort(disorder_list,low+1,last)

if __name__ == '__main__':
    test_list = [9,8,12,5,24,66,4,4,11,12,14,665,54,6126]
    quick_sort(test_list,0,len(test_list)-1)
    print(test_list)
