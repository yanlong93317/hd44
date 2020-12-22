import unittest    #引入自动化框架
from model.brower import chrome   #引入浏览器
class BaseCase(unittest.TestCase):    #定义一个类
    def setUp(self):    #定义一个函数
        self.driver=chrome()    #浏览器实例化
    def tearDown(self):
        self.driver.quit()    #浏览器退出
