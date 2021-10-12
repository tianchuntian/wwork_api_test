def test_create_data():
    """制造测试数据"""
    data = [("zhangsan" + str(i + 1), "张三" + str(i + 1), "138%08d" % (i + 1), 1, "李四" + str(i + 1)) for i in range(20)]
    print(data)
    return data