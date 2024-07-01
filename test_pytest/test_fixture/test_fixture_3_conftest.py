import pytest


def test1(my_fixture1, global_variable):
    print("\n=== test1 > {}".format(my_fixture1))
    g1 = global_variable.get("g1")
    print(f"\n=== {g1=}")
    global_variable["g1"] = "g1 1"


# fixture2有了别名之后就不能再用原来的名字了，会报错
def test2(my_fixture1, f2, global_variable):
    print("\n=== test2 > {} | {}".format(my_fixture1, f2))
    g1 = global_variable.get("g1")
    print(f"\n=== {g1=}")  # g1 还是None，因为global_variable的scope是class


def test3(my_fixture3):
    print("\n=== test3 > {}".format(my_fixture3))


class TestClassGlobeFixture:

    @pytest.mark.run(order=1)
    def test_1(self, global_variable):
        g1 = global_variable.get("g1")
        print(f"\n=== {g1=}")
        global_variable["g1"] = "g1 1"

    @pytest.mark.run(order=2)
    def test_2(self, global_variable):
        g1 = global_variable.get("g1")
        print(f"\n=== {g1=}")
        global_variable["g1"] = "g1 2"

    @pytest.mark.run(order=3)
    def test_3(self, global_variable):
        g1 = global_variable.get("g1")
        print(f"\n=== {g1=}")


if __name__ == '__main__':
    pytest.main([__file__, '-vs'])
