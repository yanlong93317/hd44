from page.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class FrameEdit(BasePage):
    snat_locator = (By.NAME, "menu")
    pro_locator = (By.XPATH, "/html/body/div[2]/div[1]/ul/li[1]/ul/li[1]/a")
    edit_locator = (By.XPATH, "//*[@id='listDiv']/table/tbody/tr[2]/td[8]/a[2]")

    def menu_frame(self):
        self.driver.switch_to.frame("menu-frame")

    def snat_loact(self):
        self.driver.find_element(*self.snat_locator).click()
        sleep(2)

    def pro_loac(self):
        self.driver.find_element(*self.pro_locator).click()
        sleep(2)

    def defa_content(self):
        self.driver.switch_to.default_content()

    def main_frame(self):
        self.driver.switch_to.frame("main-frame")

    def edit(self):
        self.driver.find_element(*self.edit_locator).click()
        sleep(2)

    def degr(self):
        # self.open()
        self.menu_frame()
        self.snat_loact()
        self.pro_loac()
        self.defa_content()
        self.main_frame()
        self.edit()
