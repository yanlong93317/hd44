from selenium.webdriver.common.by import By  # 引入By类
from page.base_page import BasePage  # 调用自己写的类
from time import sleep  # 引入时间
class loginpage(BasePage):
    # 重写url属性，父类的url+/crm拼接
    _url = BasePage._url + "/admin"
    # 页面属性
    # 用户名输入框定位器
    username_locator = (By.NAME, "username")
    # 密码输入框定位器
    password_locator = (By.NAME, "password")
    # 登录按钮定位器
    submit_locator = (By.CSS_SELECTOR,"input[value='进入管理中心']")

    def input_uesrname(self, username):
        """
        找到用户名输入框并进行输入
        :param username:
        :return:
        """
        element = self.driver.find_element(*self.username_locator)
        element.clear()
        element.send_keys(username)
        sleep(2)  # 暂时2秒

    def input_password(self, password):
        """
        找到密码输入框并进行输入
        :param password:
        :return:
        """
        element = self.driver.find_element(*self.password_locator)
        element.clear()
        element.send_keys(password)
        sleep(3)

    def sumbit(self):
        """
        用于找到确定按钮并点击
        :return:
        """
        self.driver.find_element(*self.submit_locator).click()
        sleep(3)

    def login(self, username, passwrd):  # 定义一个类，用于进行登录的一些操作
        """
        聚合函数
        :param username:
        :param passwrd:
        :return:
        """
        self.open()
        self.input_uesrname(username)
        self.input_password(passwrd)
        self.sumbit()
        sleep(2)
