def test_open_url():
    print("running open url")
    assert False


def second_test():  # 方法不能把test放后面，这条不会被执行，指定nodeId也不行
    print("running second_test")
    assert True


def test_3():
    print("running test_3")
    assert True

