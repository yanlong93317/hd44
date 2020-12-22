from page.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class Frame_remo(BasePage):
    def delll(self):
        """
        删除
        :return:
        """
        self.driver.switch_to.frame("menu-frame")  # 定位到menu-frame
        self.driver.find_element(By.XPATH, "//*[@id='menu-ul']/li[2]").click()
        self.driver.find_element(By.XPATH, "//*[@id='menu-ul']/li[2]/ul/li[1]/a").click()
        sleep(2)
        self.driver.switch_to.default_content()  # 返回到最外层
        self.driver.switch_to.frame("main-frame")
        sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='listDiv']/table/tbody/tr[2]/td[8]/a[3]").click()
        sleep(5)
        self.driver.switch_to.alert.accept()
        sleep(2)
