from page.base_page import BasePage  # 调用类


class Homepage():  # 定义一个类
    _url = BasePage._url + "/admin"  # 设置url地址

    def __init__(self, driver, url=None):  # 将类实例化
        self.driver = driver
        if not url:
            self.url = self._url
