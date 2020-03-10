

# 有序序列的查找功能
# 非递归模式下的二分查找

def binary_search(order_list,x):
    n = len(order_list)
    mid_index = n//2
    mid_value = order_list[mid_index]
    if x == mid_value:
        return mid_index
    low = 0
    high = n-1
    while  low != high:
        if x < mid_value:
            high = mid_index - 1
            mid_index = (low+high) // 2
            mid_value = order_list[mid_index]
        else:
            low = mid_index + 1
            mid_index = (low + high) // 2
            mid_value = order_list[mid_index]
        if x == mid_value:
            return mid_index
    return -1

#递归方式实现
def binary_search_by_traceback(order_list,x):
    low = 0
    high = len(order_list) - 1
    if low == high:
        return -1
    mid_index = (low+high) // 2
    mid_value = order_list[mid_index]
    if mid_value == x:
        return mid_index
    elif mid_value < x :
        binary_search_by_traceback(order_list[mid_index+1:],x)
    else:
        binary_search_by_traceback(order_list[:mid_index])

if __name__ == '__main__':
    a = [ 1, 3 , 3, 4 ,9]
    print(binary_search(a,14))
