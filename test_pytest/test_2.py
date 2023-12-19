import pytest


def test_2_1():
    print("正在执行测试模块----test_2_1")
    x = "this"
    assert 'h' in x


def test_2_2():
    print("正在执行测试模块----test_2_2")
    assert False


@pytest.mark.smoke
@pytest.mark.skip(reason="skip test")  # 无条件跳过
def test_2_3():
    print("正在执行测试模块----test_2_3")
    assert True


i = 1
@pytest.mark.smoke
@pytest.mark.skipif(i > 0, reason="skipif test")  # 有条件跳过
def test_2_4():
    print("正在执行测试模块----test_2_4")
    assert False


def test_2_5():
    print("正在执行测试模块----test_2_5")
    assert False

