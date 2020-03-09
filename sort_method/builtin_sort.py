if __name__ == '__main__':
    #正数在前，负数在后，正数从小到大，负数从大刀小
    test_list = [7, -8, 5, 4, 0, -2, -5]
    test_list.sort(key= lambda x:(x<0,abs(x)))
    print(test_list)
    # 实现年龄从大到小排列
    students = [('a',15),('b',17),('c',14)]
    students.sort(key= lambda x:x[1],reverse=True)
    print(students)
    # 实现 数字在前，字母在后，数字先奇再偶，字母先小写再大写
    s='asdf234GDSdsf23' # 排序:小写-大写-奇数-偶数
    tmp_list = list(s)
    #原理:
    # False 会排在前 True会排在后面
    # x.isdigit()的作用是把数字放在前边,字母放在后边.
    # x.isdigit() and int(x) % 2 == 0的作用是保证奇数在前，偶数在后。
    # x.isupper()的作用是在前面基础上,保证字母小写在前大写在后.
    # 最后的x表示在前面基础上,对所有类别数字或字母排序
    tmp_list.sort(key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x))
    s = "".join(tmp_list)
    print(s)