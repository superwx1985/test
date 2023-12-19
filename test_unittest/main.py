# 单元测试.py

"""
1、单元测试框架：自动校验结果
    python:unittest或者pytest、Java：Junit、TestNG
    怎么写用例：
        必须以test开头
    查找用例
    参数化
"""
import unittest, os
import myFunction
import HTMLReport
import parameterized  # 参数化


class TestAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("set up class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tear down class")

    def setUp(self) -> None:
        print("set up case")

    def tearDown(self) -> None:
        print("tear down case")

    '''测试add方法'''
    def testAddNormal1(self):
        """正常的测试加法，by huozi"""
        print("testAddNormal1")
        result = myFunction.add(1, 2)
        self.assertEqual(3, result, )

    def testAddNormal2(self):
        """正常的测试加法，带有msg返回信息"""
        print("testAddNormal2")
        result = myFunction.add(4, 2)
        self.assertEqual(6, result, '正常case通过')

    def testAddError1(self):
        """测试失败使用,by huozi"""
        print("testAddError1")
        result = myFunction.add(0, 2)
        self.assertEqual(4, result)

    def testAddError2(self):
        """测试失败使用带有msg返回信息的"""
        print("testAddError2")
        result = myFunction.add(1, 2)
        self.assertEqual(0, result, '正常整数加法，没有通过')

    @parameterized.parameterized.expand(  # 传参为二维数组
        [[1, 2, 3, '参数化1'],
         [-1, 2, 3, '参数化2'],
         [2, 4, 7, '参数化3']]
    )
    def testParamAdd(self, a, b, c, desc):
        print("testParamAdd" + desc)
        self._testMethodDoc = desc  # 使用这个_testMethodDoc参数传递
        result = myFunction.add(a, b)
        self.assertEqual(c, result, '预期结果是%s,实际结果是%s' % (c, result))


if __name__ == '__main__':
    # 写法0：不产生测试报告
    # unittest.main()  # 执行所有用例

    # 写法1：运行单个测试用例
    testSuite1 = unittest.TestSuite()
    testSuite1.addTest(TestAdd('testAddNormal1'))  # 运行单个测试用例
    # testSuite.addTest(TestAdd('testAddError1'))
    # testSuite.addTest(TestAdd('testAddError1'))

    # 写法2：运行某个类里面的测试用例
    testSuite2 = unittest.makeSuite(TestAdd)  # 运行某个类(如TestAdd)里面所有的测试用例

    # 写法3：查找某个目录下的测试用例(绝对路径)，文件必须以test开头，所有文件就是：*.py
    testSuite3 = unittest.defaultTestLoader.discover('..', 'test*.py')

    runner = HTMLReport.TestRunner(
        report_file_name="index",
        output_path=os.path.join(os.path.dirname(__file__), "report"),
        title="一个简单的测试报告",
        description="随意描述",
        thread_count=5,
        thread_start_wait=0.1,
        tries=1,
        delay=0,
        back_off=1,
        retry=True,
        sequential_execution=True,
        lang="cn"
    )
    runner.run(testSuite2)
