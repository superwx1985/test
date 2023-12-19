import pytest


def test_4():
    assert True


def test_6():
    assert True


@pytest.mark.run(order=3)
def test_5():
    assert True


def test_1():
    assert True


@pytest.mark.run(order=0)
def test_2():
    assert True


def test_3():
    assert True


if __name__ == '__main__':
    pytest.main([__file__, '-v'])  # @pytest.mark.run(order=0)用于标记优先级，数字越小优先级越高，不带标记的优先级低，按从上到下顺序执行

