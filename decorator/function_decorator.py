import functools


def repeat(n):
    def my_decorator(func):
        @functools.wraps(func)  # 内置的装饰器@functools.wrap，它会帮助保留原函数的元信息（也就是将原函数的元信息拷贝到对应的装饰器函数里）
        def wrapper(*args, **kwargs):
            print(f'wrapper of my_decorator')
            _ = list()
            for i in range(n):
                print(f'\n{i+1}\n')
                _.append(func(*args, **kwargs) + " | postfix")
            return _
        return wrapper
    return my_decorator


def greet(message, a=1, b=2):
    print(f"{message=}, {a=}")
    return f"{a} | {b}"


if __name__ == '__main__':
    # repeat4 = repeat(4)
    # new_greet = repeat4(greet)
    # new_greet('1', '2')

    @repeat(2)
    def aaa(message, a='', b=''):
        print(f"{message=}, {a=}, {b=}")
        return f"{a} | {b}"
    r = aaa('1', '2', b='b')
    print(aaa.__name__)
    print(r)
    pass
