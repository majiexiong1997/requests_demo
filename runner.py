
import unittest
import os
import time
import logging
from html_runner import HTMLTestRunner

class AllTest:
    def __init__(self):

        self.test_dir = os.path.join(os.getcwd())

        print(self.test_dir)

        self.discover = unittest.defaultTestLoader.discover(self.test_dir,pattern='test_*.py')



        self.now = time.strftime('%Y-%m-%d %H_%M_%S')
        print(self.now)

        self.result = self.test_dir+'\\result\\'+self.now+'_result.html'
        self.log = self.test_dir + '\\result\\' + self.now + '_log.txt'

        logging.basicConfig(filename=self.log,level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    def run(self):

        fp = open(self.result,'wb')
        print('try')

        runner = HTMLTestRunner(stream=fp, title='测试报告', description='aguest_master项目用例执行情况',verbosity=2)

        runner.run(self.discover)
        print('end')

        fp.close()


if __name__ == '__main__':
    AllTest().run()