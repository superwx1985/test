#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
微信公众号：AllTests软件测试
"""

import pytest


# 参数化（优化代码）
@pytest.mark.parametrize("test_input, expected", [("3+4", 9), ("2+5", 7), ("6*9", 48)])
def test_eval(test_input, expected):
    print(f"测试数据{test_input}, 预期结果{expected}")
    assert eval(test_input) == expected


@pytest.mark.parametrize(["name", "pwd"], [("AllTests", "123456"), ("qq", "85135506")])
def test_parametrize_case1(name, pwd):
    print(name, pwd)


my_data = [(1, 2, 3), (4, 5, 9)]

ids = [f"a:{a} + b:{b} = expect:{expect}" for a, b, expect in my_data]


# 给参数值取个id，防止参数过长或者是中文时报告内容不好看
@pytest.mark.parametrize("a, b, expect", my_data, ids=ids)
def test_parametrize_case2(a, b, expect):
    print("测试数据为{}-{}".format(a, b))
    assert a + b == expect


# 参数化测试类
my_data = [(1, 2, 3), (4, 5, 9)]


@pytest.mark.parametrize("a, b, expect", my_data)
class TestParametrize:
    def test_parametrize_case1(self, a, b, expect):
        print("\n测试用例case1 测试数据为{}+{}".format(a, b))
        assert a + b == expect

    def test_parametrize_case2(self, a, b, expect):
        print("\n测试用例case2 测试数据为{}+{}".format(a, b))
        assert a + b == expect


# 当参数化装饰器有很多个的时候，用例数等于n(个)*n(个)*n(个)*n(个)*....
my_data_1 = [(1, 2), (3, 4), (5, 6)]
my_data_2 = ["a", "b"]


@pytest.mark.parametrize("a, b", my_data_1, ids=[f"{a=}, {b=}" for a, b in my_data_1])
@pytest.mark.parametrize("c", my_data_2, ids=(f"{c=}" for c in my_data_2))
def test_parametrize_case3(a, b, c):
    print(f"测试数据为：{a}，{b}, {c}")


# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
微信公众号：AllTests软件测试
"""

import pytest

my_data = (
    {
        "user": "AllTests",
        "pwd": "123456"
    },
    {
        "user": "wangmcn",
        "pwd": "567890"
    }
)


# @pytest.mark.parametrize('dic', my_data, ids=(f"{d['user']=}, {d['pwd']=}" for d in my_data))
@pytest.mark.parametrize('dic', my_data, ids=((f"{d.items()=}" for d in my_data)))
def test_parametrize_case(dic):
    print(f'user:{dic["user"]}, pwd:{dic["pwd"]}')


if __name__ == '__main__':
    pytest.main([__file__, '-s'])
