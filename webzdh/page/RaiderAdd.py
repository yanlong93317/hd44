from selenium.webdriver.common.by import By
# from selenium import webdriver
from page.base_page import BasePage
from time import sleep
class AddRaider(BasePage):
    """
    类的定位器
    """
    nameActivity_locator=(By.XPATH,"/html/body/div[1]/form/table/tbody/tr[1]/td[2]/input")
    shangpKeyword_locator=(By.NAME,"keywords")
    search_locator=(By.CSS_SELECTOR,"input[value=' 搜索 ']")
    describe_locator=(By.NAME,"desc")
    confirm_locator=(By.CSS_SELECTOR,"input[value=' 确定 ']")

    def input_nameActivity(self,name_activity):
        """
        活动名称
        :param name_activity:
        :return:
        """
        element=self.driver.find_element(*self.nameActivity_locator)
        element.clear()
        element.send_keys(name_activity)
        sleep(3)
    def input_shangpKeyword(self,shangp_keyword):
        """
        商品关键字
        :param shangp_keyword:
        :return:
        """
        eleme=self.driver.find_element(*self.shangpKeyword_locator)
        eleme.clear()
        eleme.send_keys(shangp_keyword)
        sleep(3)
    def input_search(self):
        """
        商品关键字
        :return:
        """
        self.find_element(self.search_locator).click()
        sleep(1)
    def input_describe(self,describe):
        """
        描述
        :param describe:
        :return:
        """
        eme=self.driver.find_element(*self.describe_locator)
        eme.clear()
        eme.send_keys(describe)
        sleep(2)
    def queding_locator(self):
        """
        确定按钮
        :return:
        """
        self.find_element(self.confirm_locator).click()
        sleep(3)
    def input(self,nameActivity,shangpKeyword,describe):
        """
        聚合函数
        :param nameActivity:
        :param shangpKeyword:
        :param describe:
        :return:
        """
        self.input_nameActivity(nameActivity)
        self.input_shangpKeyword(shangpKeyword)
        self.input_search()
        self.input_describe(describe)
        self.queding_locator()

