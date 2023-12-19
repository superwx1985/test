# 是单独存放的一个夹具配置文件, 可以跨module使用
# 原则上应该放在用例的同一路径，但实际上父级也可以调用到
# 如果多级同时存在，则取最靠近的那个
import pytest


@pytest.fixture(params=[1, 1465454564646])
def my_fixture1(request):
    print("\n=== my_fixture1 before")
    yield request.param  # 注意这里param没有s
    print("\n=== my_fixture1 after")
    return


# 给这个fixture起个别名叫f2
@pytest.fixture(params=("b", "中文1"), name="f2")
def my_fixture2(request):
    print("\n=== my_fixture2")
    return request.param


# 给参数值取个id，防止参数过长或者是中文时报告内容不好看
@pytest.fixture(params=("中文2", "中文3"), ids=("zw2", "zw3"))
def my_fixture3(request):
    print("\n=== my_fixture3")
    return request.param
