import pytest


# 自定义前后置方法
'''
params：参数化，支持列表，元祖，字典列表[{}, {}]，字典元祖({}, {})
'''
@pytest.fixture(params=[0, 1465454564646])
def my_fixture1(request):
    print("\n=== my_fixture1 before")
    yield request.param  # 注意这里param没有s
    print("\n=== my_fixture1 after")
    return


# 给这个fixture起个别名叫f2
@pytest.fixture(params=("a", "中文1"), name="f2")
def my_fixture2(request):
    print("\n=== my_fixture2")
    return request.param


# 给参数值取个id，防止参数过长或者是中文时报告内容不好看
@pytest.fixture(params=("中文2", "中文3"), ids=("zw2", "zw3"))
def my_fixture3(request):
    print("\n=== my_fixture3")
    return request.param


def test1(my_fixture1):
    print("\n=== test1 > {}".format(my_fixture1))


# fixture2有了别名之后就不能再用原来的名字了，会报错
def test2(my_fixture1, f2):
    print("\n=== test2 > {} | {}".format(my_fixture1, f2))


def test3(my_fixture3):
    print("\n=== test3 > {}".format(my_fixture3))


if __name__ == '__main__':
    pytest.main([__file__, '-vs'])
