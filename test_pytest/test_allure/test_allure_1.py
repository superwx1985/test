import os

import pytest


# 测试模块中的用例1
def test_one():
    print("正在执行测试模块----test_one")
    x = "this"
    assert 'h' in x


# 测试模块中的用例2
def test_two():
    print("正在执行测试模块----test_two")
    assert False


# 测试类
class TestCase1:
    def test_three(self):
        print("正在执行测试类----test_three")
        x = "this"
        assert 'h' in x

    def test_four(self):
        print("正在执行测试类----test_four")
        x = dict()
        assert hasattr(x, 'pop')


# 测试类
class TestCase2:
    def test_five(self):
        assert True

    def test_five_2(self):
        assert False

    def test_six(self):
        assert True


if __name__ == '__main__':
    pytest.main()
    os.system("allure generate ./temp -o ./report --clean")
