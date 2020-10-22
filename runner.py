import unittest
import os
import time
import logging
from html_runner import HTMLTestRunner
from config import getpathinfo

path = getpathinfo.get_path()
print(path)
report_path = os.path.join(path, 'result')
class AllTest:
    def __init__(self):
        global report_path
        self.test_dir = os.path.join(os.getcwd())

        print(self.test_dir)

        # self.discover = unittest.defaultTestLoader.discover(self.test_dir, pattern='test_*.py')
        self.caseListFile = os.path.join(self.test_dir+'\\test_case',"caselist.txt")  #需要执行的接口文件汇总路径
        self.caseFile = os.path.join(self.test_dir, "test_case")
        self.resultPath = os.path.join(self.test_dir+'\\result', "report.html")  #报告路径
        self.caseList = []


        self.now = time.strftime('%Y-%m-%d %H_%M_%S')


        if not getpathinfo.get_result_path() == []:  # 判断是否有报告，如果有删除之前的生成最新的，如果没有直接执行
            for file in getpathinfo.get_result_path():
                os.remove(self.test_dir + '\\result\\' + file)
            self.result = self.test_dir + '\\result\\' + self.now + '_result.html'
            self.log = self.test_dir + '\\result\\' + self.now + '_log.txt'

            logging.basicConfig(filename=self.log, level=logging.INFO,
                                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        else:

            self.result = self.test_dir + '\\result\\' + self.now + '_result.html'
            self.log = self.test_dir + '\\result\\' + self.now + '_log.txt'

            logging.basicConfig(filename=self.log, level=logging.INFO,
                                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def set_case_list(self):
        """
        读取caselist.txt文件中的用例名称，并添加到caselist元素组
        :return:
        """
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):  # 如果data非空且不以#开头
                self.caseList.append(data.replace("\n", ""))  # 读取每行数据会将换行转换为\n，去掉每行数据中的\n

    def set_case_suite(self):
        '''
        添加用例组，并批量加载用例
        :return:
        '''
        self.set_case_list()  # 通过set_case_list()拿到caselist元素组
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in self.caseList:  # 从caselist元素组中循环取出case
            case_name = case.split("/")[-1]  # 通过split函数来将aaa/bbb分割字符串，-1取后面，0取前面
            print(case_name + ".py")  # 打印出取出来的名称
            # 批量加载用例，第一个参数为用例存放路径，第一个参数为路径文件名
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            suite_module.append(discover)  # 将discover存入suite_module元素组
            print('suite_module:' + str(suite_module))
        if len(suite_module) > 0:  # 判断suite_module元素组是否存在元素
            for suite in suite_module:  # 如果存在，循环取出元素组内容，命名为suite
                for test_name in suite:  # 从discover中取出test_name，使用addTest添加到测试集
                    test_suite.addTest(test_name)
        else:
            print('else:')
            return None
        return test_suite



    def run_test(self):

        suit = self.set_case_suite()# 调用set_case_suite获取test_suite
        print('========')
        print(suit)
        print('========')
        print('try')

        print(str(suit))
        try:
            if suit is not None:  # 判断test_suite是否为空
                print('if-suit')
                fp = open(self.result, 'wb')  # 打开result/20181108/report.html测试报告文件，如果不存在就创建
                # 调用HTMLTestRunner
                runner = HTMLTestRunner(stream=fp, title='测试报告', description='aguest_master项目用例执行情况', verbosity=2)
                runner.run(suit)
            else:
                print("Have no case to test.")
        except Exception as ex:
            print(str(ex))
            logging.info(str(ex))




if __name__ == '__main__':
    AllTest().run_test()
