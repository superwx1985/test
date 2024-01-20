import pytest
import datetime

if __name__ == "__main__":
    # pytest.main()  # 无参运行，注意可能会被配置文件pytest.ini干扰
    # pytest.main(['-v'])  # 详细信息
    # pytest.main(['-s'])  # 显示打印的信息
    # pytest.main(['test_2.py'])  # 只执行某个模块
    # pytest.main(['test_ui/', '-s'])  # 只执行某个package
    # pytest.main(['-v', 'test_folder/3_test.py::test_3_1'])  # 通过nodeID执行
    pytest.main(['-v', 'test_folder/3_test.py::aaa_3_2_test'])  # 方法不能把test放后面，指定nodeId也不行，会报错
    # pytest.main(['-v', 'test_1.py::TestCase::test_three'])  # 通过nodeID执行，类方法
    # pytest.main(['-v', 'test_2.py', '-x'])  # 遇到一个失败的就停止执行
    # pytest.main(['-v', 'test_2.py', '--maxfail=2'])  # 遇到一个失败的就停止执行
    # pytest.main(['-v', 'test_1.py', '-k=_t'])  # 只执行名字包含字符串“_t”的用例
    # pytest.main(['-v', '-m smoke or login'])  # 执行带 smoke 或者 login 的用例，但是因为没注册自定义标记，会出现警告
    # pytest.main(['-v', "--html=reports/report.html"])
    # pytest.main(['-v', '-m smoke or login', "--html=./reports/report {}.html".format(str(datetime.datetime.now()).replace(":", ".")[:-7])])
    pass

