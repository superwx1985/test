from time import sleep
import pytest


def test_1():
    sleep(5)
    assert True


def test_2():
    sleep(1)
    assert True


@pytest.mark.smoke
def test_3():
    assert True


def test_4():
    assert True


def test_5():
    assert True


@pytest.mark.login
def test_6():
    assert True


@pytest.mark.smoke
def test_7():
    assert False


if __name__ == '__main__':
    # pytest.main([__file__, '-v'])  # 同步执行
    pytest.main([__file__, '-v', '-n=2'])  # 异步执行，参数n不要和其他参数一起，n后面跟线程数，依赖pytest-xdist
    # pytest.main([__file__, '-v', '-n 2'])  # 异步执行，另一种写法
