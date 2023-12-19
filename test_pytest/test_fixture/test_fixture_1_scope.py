import pytest


# 自定义前后置方法
'''
@pytest.fixture(scope="", params="", autouse=False, ids="", name="")
scope：表示的是被@pytest.fixture标记的方法的作用域。function(默认)，class，module，package/session.
params：参数化，支持列表，元祖，字典列表，字典元祖
autouse：是否自动使用，即不用主动调用也会使用，默认False
ids：当使用params参数化时，给每一个值设置一个变量名。意义不大
name：给被@pytest.fixture标记的方法取一个别名
'''
@pytest.fixture()
def my_fixture1():
    print("\n=== my_fixture1 before")
    yield
    print("\n=== my_fixture1 after")


@pytest.fixture(autouse=True)
def my_fixture2():
    yield
    print("\n=== my_fixture2 after")


@pytest.fixture(scope="class", autouse=True)
def my_fixture3():
    print("\n=== my_fixture3")


i = 0
@pytest.fixture()
def my_fixture4(scope="session"):
    print("\n=== my_fixture3")
    global i
    i += 1
    return i  # 传递一个整个session期间生效的变量


def setup_function():
    print("\n=== 前置函数")


def teardown_function():
    print("\n=== 后置函数")


def test1(my_fixture1):
    print("\n=== test1")


def test2():
    print("\n=== test2")


class TestClass1:
    def test3(self):
        print("\n=== test3")

    def test4(self, my_fixture4):
        print("\n=== test4 > {}".format(my_fixture4))

    def test5(self, my_fixture4):
        print("\n=== test5 > {}".format(my_fixture4))


if __name__ == '__main__':
    pytest.main([__file__, '-vs'])
