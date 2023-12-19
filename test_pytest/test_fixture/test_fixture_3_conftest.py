import pytest


def test1(my_fixture1):
    print("\n=== test1 > {}".format(my_fixture1))


# fixture2有了别名之后就不能再用原来的名字了，会报错
def test2(my_fixture1, f2):
    print("\n=== test2 > {} | {}".format(my_fixture1, f2))


def test3(my_fixture3):
    print("\n=== test3 > {}".format(my_fixture3))


if __name__ == '__main__':
    pytest.main([__file__, '-vs'])
