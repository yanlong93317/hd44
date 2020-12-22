from selenium.webdriver.remote.webelement import WebElement


class BasePage():
    _url = "http://192.168.1.134:8080/upload"  # 基类存放服务器地址

    def __init__(self, driver, url=None):  # 类实例化
        self.driver = driver
        if not url:
            url = self._url
        self.url = url

    def open(self):  # 定义一个函数，用于打开网页
        self.driver.get(self.url)

    def find_element(self, locator, element=None):
        """
        查找元素,要求传入定位器，如果只传入定宁器,整个浏伤器里面找。
        如果传入定位器,并且传入了一个元素对象，再这个元素的基础上再查找元素|
        :param locator:
        :param element:
        :return:
        """
        if element and isinstance(element, WebElement):
            return element.find_element(*locator)
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        self.driver.find_element(*locator)
