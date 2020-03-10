


#归并排序 从小到大，递归一个列表，返回一个有序列表
#时间复杂度 O (nlogn)
def merge(disorder_list):
    n = len(disorder_list)
    if n <= 1:
        return disorder_list
    mid = n // 2
    left_order_list = merge(disorder_list[:mid])
    right_order_list = merge(disorder_list[mid:])
    left_pointer = 0
    right_pointer = 0
    results = []
    while left_pointer < len(left_order_list)  and right_pointer < len(right_order_list) :
        if left_order_list[left_pointer] < right_order_list[right_pointer]:
            results.append(left_order_list[left_pointer])
            left_pointer += 1
        else:
            results.append(right_order_list[right_pointer])
            right_pointer += 1
    results += left_order_list[left_pointer:]
    results += right_order_list[right_pointer:]
    return results

if __name__ == '__main__':
    test_list = [9,8,12,5,24,66,4,4,11,12,14,665,54,6126]
    a = merge(test_list)
    print(a)
