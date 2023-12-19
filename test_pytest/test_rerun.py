import pytest


def test_1():
    assert True


i = 0


def test_2():
    global i
    if i < 2:
        print("i = {}".format(i))
        i += 1
        assert False
    else:
        print("i = {}".format(i))
        assert True


if __name__ == '__main__':
    pytest.main([__file__, '-vs', '--reruns=2'])  # 注意是两个横线，而且只能用等号连接重跑次数
